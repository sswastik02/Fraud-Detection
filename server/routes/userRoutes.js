const express = require('express')
const {
  signUpUser,
  signInUser,
  getUser,
  getAllUsers
} = require('../controller/user.controller')
const {verifyUser} = require('../middleware/middleware')
const router = express.Router()

router.post('/signup', signUpUser)
router.post('/signin', signInUser)
router.get('/getallusers', getAllUsers)
router.route('/me').get([verifyUser], getUser)

module.exports = router
