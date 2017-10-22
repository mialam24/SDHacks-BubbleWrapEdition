var mongoose = require('mongoose');

var dburl = 'mongodb://localhost:27017/fridgeData';

mongoose.connect(dburl);

mongoose.connection.on('connected', function(){
	console.log('Connected to db');
});
mongoose.connection.on('error', function(err) {
  console.log('Mongoose connection error: ' + err);
});
mongoose.connection.on('disconnected', function() {
  console.log('Mongoose disconnected');
});


function gracefulShutdown(msg, callback) {
  mongoose.connection.close(function() {
    console.log('Mongoose disconnected through ' + msg);
    callback();
  });
}

process.on('SIGINT', function() {
  gracefulShutdown('App termination (SIGINT)', function() {
    process.exit(0);
  });
});
require('./fridgeItem.model.js');