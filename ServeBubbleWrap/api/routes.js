var router = require('express').Router();

var dataController = require('./controllers/dataController.js');

router
  .route('/in')
  .post(dataController.itemIn);

router
  .route('/out')
  .post(dataController.itemOut);

router
  .route('/name')
  .post(dataController.getByName);

 router
   .route('/count')
   .post(dataController.getCount);

 router
   .route('/all')
   .post(dataController.getAllByLabel)
   .get(dataController.getAll);

 module.exports = router;