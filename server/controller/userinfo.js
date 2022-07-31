const userData = require('../models/User')
const express = require('express')
const apicall = require('../routes/apicall')
const phishing = require('../controller/apicall.controller')

const data =    
  {
    "merchant_id":3799132406,
    "avg_amount_days":642.6249223,
    "amount":14780.37321,
    "is_declined":false,
    "number_declined_days":0,
    "foreign_transaction":false,
    "high_risk_countries":false,
    "daily_chbk_avg_amt": 718,
    "sixm_avg_chbk_amt": 175,
    "sixm_chbk_freq": 5
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
                let y = {fraud:result.data.fraud , user : user}
                res.json(y)
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