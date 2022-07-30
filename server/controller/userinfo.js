const userData = require('../models/User')

const getUserInfo = async (req, res) => {
    try {
      const userinfo = await userData.find({ _id : req.params.id})
      console.log(userinfo)
      userData.findById( req.params.id)
      .then((user) =>{
            user.firstname = req.body.firstname;
            user.lastname = req.body.lastname;
            user.address = req.body.address;
            user.city = req.body.city;
            user.country = req.body.country;
            user.zipcode = req.body.zipcode;
            user.cardholderName = req.body.cardholderName;
            user.cardNumber = req.body.cardNumber;
            user.aadharURL= req.body.aadharURL;
            user.age = req.body.age;
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