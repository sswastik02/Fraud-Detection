const userData = require('../models/User')
const express = require('express')
const apicall = require('../routes/apicall')
const phishing = require('../controller/apicall.controller')

const data = {    
    
  "merchant_id":3799132406,
  "avg_amount_days":780.3223403,
  "amount":39016.11702,
  "is_declined":false,
  "number_declined_days":5,
  "foreign_transaction":true,
  "high_risk_countries":true,
  "daily_chbk_avg_amt": 0,
  "sixm_avg_chbk_amt": 0,
  "sixm_chbk_freq": 0

  
}

const getUserInfo = async (req, res) => {
  try {
    const userinfo = await userData.find({ _id : req.params.id})
    console.log(userinfo)
    userData.findById( req.params.id)
    .then((user) =>{
          user.firstname = req.body.firstname;
          user.lastname = req.body.lastname;
          user.address = req.body.address;
          user.zipcode = req.body.zip;
          user.city = req.body.city;
          user.country = req.body.country;
          user.cardholderName = req.body.cardholdername;
          user.cardNumber = req.body.card;
          user.save()  
          .then((user) =>{
            // res.statusCode = 200;
            // res.setHeader('Content-Type', 'application/json');
            phishing(data)
              .then((result)=>{
              
                console.log(result.data.fraud);
                res.json(result.data.fraud)
              })
            // res.json(user);
          })
    })
   
  } catch (err) {
    console.log(err)
    sendResponseError(500, `Error ${err}`, res)
  }
}

module.exports =  getUserInfo 