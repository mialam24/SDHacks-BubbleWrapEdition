var mongoose = require('mongoose');

var studentSchema = new mongoose.Schema({
	firstName : String,
	lastName : String,
	phone : {
		type: String,
		required: true,
		unique: true
	},
	subject : String,
	subjectNumber : String,
	topic : String,
	status : String
});

mongoose.model('Student', studentSchema);