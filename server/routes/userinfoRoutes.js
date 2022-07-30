const express = require("express");
const router = express.Router();
const  userInfo = require("../controller/userinfo");
router.put('/:id', userInfo);
module.exports = router;