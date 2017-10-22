var mongoose = require('mongoose');

var fridgeItemSchema = new mongoose.Schema({
	name : String,
	label : String,
	dateStored : String, //mm-dd-yyyy
	dateExp : String //mm-dd-yyyy
});

mongoose.model('fridgeItem', fridgeItemSchema);