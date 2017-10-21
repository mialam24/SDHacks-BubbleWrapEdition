var mongoose = require('mongoose');
var Student = mongoose.model('Student');

module.exports = {
	smsRecieveText: smsRecieveText,
};

function smsRecieveText(req, res) {
	console.log(`Recieved Text`);
	console.log(req.body);

	/**
	 *Redirect the text based on the response
	 */
	 redirectText(req, res);

	
};

function redirectText(req, res) {
	/*
	 *Check if first time visiter
	 */

	 var phoneNum = req.body.From;
	 Student
	   .findOne({phone: phoneNum}) //Search for matching # in DB
	   .exec(function (err, docs) {
	   	  if (err)
	   	  	throw err;
	   	  else if (docs) { 			//If found, # exists in DB
	   	  	console.log(`${docs.phone} is not a first time visitor`);
	   	  	
	   	  	//Check which processing stage it's in
	   	  	var status = docs.phone;

	   	  	//get their name
	   	  	if (docs.status == 'get name') {
	   	  		console.log('redirecting to get name');
	   	  		getName(req, res);
	   	  	}

	        
	   	  } else {					//if not found, then # is first time visitor
	   	  	console.log(`${phoneNum} is a first time visitor`);
	   	  	console.log(`Redirecting Text to firstVisit()`);
			firstVisit(req, res);
	   	  }

	   });


}

function firstVisit(req, res) {
	console.log(`inside firstVisit()`);
	console.log(`sending text requesting for name`);

	Student
    .create({
      phone : req.body.From,
      status : 'get name'
    }, function(err, student) {
      if (err) {
        console.log("Error creating student");
        res.end();
      } else {
        console.log("student created!", student);
        res.set('Content-Type', 'text/plain');
		res.send(`Hello! What is your first and last name? (eg. John Doe)`);
		console.log('text sent');
      }
    });
}

function getName(req,res) {
	//process text and validate
	var text = req.body.Body;
	text = text.split(' ');
	if (text.length != 2) {
		console.log('name is not in correct format');
	}
	else {
		
	}


}

function joinQueue(req, res) {
	console.log(`inside joinQueue()`);
	console.log(`adding ${req.body.From} to the queue`);

	Student
    .create({
      phone : req.body.From,
      subject : req.body.Subject,
      subjectNumber : req.body.SubjectNumber,
      topic : req.body.Topic
    }, function(err, student) {
      if (err) {
        console.log("Error creating student");
        res
          .status(400)
          .json(err);
      } else {
        console.log("student created!", student);
        res
	  	  .status(201)
	  	  .json({message: `${req.body.From} added to Queue`});
      }
    });
	

}