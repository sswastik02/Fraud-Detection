const userData = require('../models/User')
const cloudinary = require('cloudinary')
require('dotenv').config()
cloudinary.config({
    cloud_name: process.env.CLOUD_NAME,
    api_key: process.env.API_KEY,
    api_secret: process.env.API_SECRET
  });
const getAadharInfo = async (req, res) => {
  try {
    const fileStr = req.body.data;
    // const uploadResponse = await cloudinary.uploader.upload(fileStr, {
    //     upload_preset: 'dev_setups',
    // });
    console.log(fileStr);
    const uploadResponse = await cloudinary.uploader.upload(fileStr ,
        result => {
            console.log(result)
            if (result) {
                res.writeHead(200, { 'content-type': 'text/plain' });
                userData.findById(req.params.id)
                .then((user) => {
                    res.statusCode = 200;
                    user.aadharURL = result;
                    console.log(user.aadharURL)
                },
                (err) => next(err))
                .catch((err) => next(err));
                res.write('received upload:\n\n')
            }
                console.log(uploadResponse);
                res.json({ msg: 'yaya' });
  
      });
    }
    catch (err) {
    console.log(err)
    sendResponseError(500, `Error ${err}`, res)
  }
}

module.exports =  getAadharInfo 