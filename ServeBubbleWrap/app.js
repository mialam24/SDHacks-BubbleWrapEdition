require('./api/data/db.js');
var express = require('express');
var bodyParser = require('body-parser');

var app = express();

app
  .get('/', function(req, res) {
	console.log(req.method, req.path)
	res
	  .status(200)
	  .json({
	  	message: "get received"
	});
  });

app.use(bodyParser.urlencoded({ extended: false }))

var router = require('./api/routes.js');

app.use('/api', router);



app.listen(3000); 
console.log("MAGIC happens on port 3000");