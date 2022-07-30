const userData = require('../models/User')

const getAadharInfo = async (req, res) => {
  try {
    const userinfo = await userData.find({ _id : req.params.id})
    console.log(userinfo)
    userData.findById( req.params.id)
    .then((user) =>{
          user.aadharURL = req.body.aadharURL;
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

module.exports =  getAadharInfo 