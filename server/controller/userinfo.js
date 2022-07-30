const userData = require('../models/User')

const getUserInfo = async (req, res) => {
    try {
      console.log(req.user.id)
      const userinfo = await userData.find({ _id : req.user.id})
      console.log(userinfo)
      userData.findById( req.params.id)
      .then((user) =>{
            user.firstname = req.body.firstname;
            user.lastname = req.body.lastname;
            user.address = req.body.address;
            user.city = req.body.city;
            user.country = req.body.country;
            user.zipcode= req.body.zip;
            user.cardholderName = req.body.cardholdername;
            user.cardNumber = req.body.card;
            user.save()  
            .then((user) =>{
              res.statusCode = 200;
              res.setHeader('Content-Type', 'application/json');
              res.json(user);
            })
      })
     
    } catch (err) {
      console.log(err)
      sendResponseError(500, `Error ${err}`, res)
    }
  }

module.exports =  getUserInfo 