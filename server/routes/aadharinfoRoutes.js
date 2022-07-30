const express = require("express");
const router = express.Router();
const  aadharInfo = require("../controller/aadharinfo");
router.put('/:id', aadharInfo);
module.exports = router;