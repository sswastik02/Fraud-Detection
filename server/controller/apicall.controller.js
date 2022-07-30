const axios = require('axios')
require('dotenv').config()
const data = {
    
    headers:{
        'Authorization' :`Api-Key ${process.env.api_url}`,
        },
    body:{
        'url' : 'google.com',
        }
    
}
 const phising =  async () =>{
    console.log(process.env.api_url)
    await axios.post('http://127.0.0.1:8000/api/phishingurl/detect' , {
    headers:{
        'Authorization' :`Api-Key ${process.env.api_url}`,
        },
    body:{
        'url' : 'google.com',
        }
    }).then( (res) =>{
        console.log(res);
    }).catch((err) =>{
        console.log(err)
    })
 } 

module.exports = phising