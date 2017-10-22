var router = require('express').Router();

var dataController = require('./controllers/dataController.js');

router
  .route('/in')
  .post(dataController.itemIn);

router
  .route('/out')
  .post(dataController.itemOut);

router
  .route('/')
  .get(function (req,res) {
  	console.log("get!");
  	res.end("hi");
  });

 module.exports = router;