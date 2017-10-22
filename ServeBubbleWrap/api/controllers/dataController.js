var mongoose = require('mongoose');
var fridgeItem = mongoose.model('fridgeItem');

module.exports = {
	itemIn: itemIn, // by object
	itemOut: itemOut, // by name
	getByName: getByName, //get an object
	getCount: getCount, // by label
	getAllByLabel: getAllByLabel,
	getAll: getAll,

};

function itemIn(req, res) {
	console.log(`Received store request`);
	console.log(req.body);
	
	name = req.body.name;
	dateStored = req.body.dateStored;
	dateExp = req.body.dateExp;
	fridgeItem.create({
		name: name,
		dateStored: dateStored,
		dateExp: dateExp
	}, function (err, fridgeItem) {
		if (err) {
			console.log(`error creating ${name}`);
			res.end('error!');
		}
		else {
			console.log(`${name} created!`);
			res.end();
		}
	});
};

function itemOut(req, res) {

}


function getByName(req, res) {
	var name = req.body.name;
	fridgeItem.findOne({name: name}, function (err, item) {
		if (err) {
			res.json({message: "woops!"});
		}
		else if (item) {
			res.json(item);
		}
		else
			res.json({message: "none"});
	});

}

function getCount(req, res) {

}

function getAllByLabel(req, res) {

}

function getAll(req, res) {

}