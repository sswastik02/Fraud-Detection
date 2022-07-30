const axios = require('axios')
require('dotenv').config()
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
 const phising =  async () =>{
    console.log(process.env.api_url)
    let data123
    await axios.post('http://127.0.0.1:8000/api/transactions/detect' , data ,{
    headers:{
        'Authorization' :`Api-Key ${process.env.api_url}`,
        }
    }).then( (result) =>{
        data123 = result
   
        
    }).catch((err) =>{
        console.log(err)
    })
    return data123
 } 

module.exports = phising