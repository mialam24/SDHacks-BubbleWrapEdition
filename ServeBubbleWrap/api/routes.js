var router = require('express').Router();

var smsController = require('./controllers/smsController.js');

router
  .route('/sms')
  .post(smsController.smsRecieveText);

 module.exports = router;