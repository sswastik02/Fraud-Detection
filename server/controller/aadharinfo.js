const userData = require('../models/User')
const cloudinary = require('cloudinary')
// const formidable = require('for')
const axios = require('axios')
require('dotenv').config()
cloudinary.config({
    cloud_name: process.env.CLOUD_NAME,
    api_key: process.env.API_KEY,
    api_secret: process.env.API_SECRET
  });
const getAadharInfo = async (req, res) => {
    
  try {
   
    // const form = new Formidable();
      const fileStr = req.body.body;
      const image= JSON.parse(fileStr)
      
      // const uploadResponse = await cloudinary.uploader.upload(fileStr, {
      //     upload_preset: 'dev_setups',
      // });
      // console.log(uploadResponse);
       // res.json({ msg: 'yaya' });
        const uploadResponse = await cloudinary.uploader.upload(image.data ,
        result => {
            if (result) {
                userData.findById(req.params.id)
                .then((user) => {
                    user.aadharURL = result.url;
                    // console.log(user.email)
                    // console.log(result.url)
                    // console.log(user.aadharURL)
                    let data = {
                      url: user.aadharURL
                    }
                    // console.log(data)
                    urlaadhar(data)
                    .then((resp)=>{
                      console.log(resp)
                      user.save()  
                      .then((user) =>{
                        res.statusCode = 200;
                        res.json(resp);
                      },
                      (err) => next(err))
                      .catch((err) =>  console.log(err));
                      })
                    })
                    

                    
               
            }  
        });

    }


    catch (err) {
    console.log(err)
   // sendResponseError(500, `Error ${err}`, res)
  }
}

const urlaadhar =  async (data) =>{
  
  let data123
  await axios.post('http://127.0.0.1:8000/api/document/verify' , data ,{
  headers:{
      'Authorization' :`Api-Key ${process.env.api_url}`,
      }
  }).then( (result) =>{
      data123 = result
      console.log(data123.data)
      
  }).catch((err) =>{
      console.log(err)
  })
  return data123.data
} 

module.exports =  getAadharInfo 