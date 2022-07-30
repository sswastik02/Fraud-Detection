const mongoose = require('mongoose')

const userSchema = new mongoose.Schema(
  {
    email: {
      type: String,
      unique: true,
      required: true,
    },
    password: {
      type: String,
      required: true,
    },
    firstname :{
      type : String
    },
    lastname :{
      type : String
    },
    zipcode :{
      type : String
    },
    address :{
      type : String
    },
    city :{
      type : String
    },
    country :{
      type : String
    },
    cardholderName :{
      type : String
    },
    cardNumber :{
      type : String
    },
    aadharURL :{
      type : String
    },
    age :{
      type : Number
    }

    

  },
  {
    timestamps: true,
  },
)

const User = mongoose.model('user', userSchema)
module.exports = User
