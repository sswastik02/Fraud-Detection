const axios = require('axios')
require('dotenv').config()
const data = {    
    
    
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
 const phising =  async (data) =>{

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