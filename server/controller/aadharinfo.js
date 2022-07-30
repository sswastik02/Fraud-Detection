const userData = require('../models/User')
const cloudinary = require('cloudinary')
require('dotenv').config()
cloudinary.config({
    cloud_name: process.env.CLOUD_NAME,
    api_key: process.env.API_KEY,
    api_secret: process.env.API_SECRET
  });
const getAadharInfo = async (req, res) => {
    console.log('helloo')
  try {
      const fileStr = req.body.fileStr;
      // const uploadResponse = await cloudinary.uploader.upload(fileStr, {
      //     upload_preset: 'dev_setups',
      // });
      // console.log(uploadResponse);
       // res.json({ msg: 'yaya' });
        const uploadResponse = await cloudinary.uploader.upload(fileStr ,
        result => {
            if (result) {
                userData.findById(req.params.id)
                .then((user) => {
                    user.aadharURL = result.url;
                    console.log(user.aadharURL)
                    user.save()  
                    .then((user) =>{
                      res.statusCode = 200;
                      res.json(user);
                    })
                },
                (err) => next(err))
                .catch((err) => next(err));
            }  
        });
    }
    catch (err) {
    console.log(err)
    sendResponseError(500, `Error ${err}`, res)
  }
}

module.exports =  getAadharInfo 