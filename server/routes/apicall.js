const express = require('express')
const phising = require('../controller/apicall.controller')
const router = express.Router()

router
  .route('/')
  .get(phising)

module.exports = router