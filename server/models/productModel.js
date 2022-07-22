var mongoose = require('mongoose')
var Schema = mongoose.Schema
var productSchema = new Schema({
    product_id : {
        type: String,
        required : true
    },
    product_name : {
        type : String,
        required : true
    },
    product_price :{
        type: Number,
        required : true
    },
    vendor_name:{
        type : String,
        required : true
    }
})

