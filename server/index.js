require('dotenv').config()
const mongoose = require('mongoose')
var http = require('http')
var express = require('express')
const port = 5000
var hostname = 'locahost'
var logger = require('morgan')
var app = express()
const server = http.createServer(app)
const url = process.env.db_url
mongoose.connect(url,{useNewUrlParser: true, useUnifiedTopology: true})
 .then((result)=>
    server.listen((port),function(){
        console.log(`Server started at http://localhost:${port}`)
    })
  )
app.use( logger('dev'))
app.use(express.json());
app.use(express.urlencoded({ extended: false }));