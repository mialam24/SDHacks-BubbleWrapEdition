var mongoose = require('mongoose');
var fridgeItem = mongoose.model('fridgeItem');

module.exports = {
	itemIn: itemIn, // by object
	itemOut: itemOut, // by name
	getByName: getByName, //get an object
	getCount: getCount, // by label
	getAllByLabel: getAllByLabel, //duh
	getAll: getAll, //EVERYTHING!!!

};

function itemIn(req, res) {
	console.log(`Received store request`);
	console.log(req.body);
	
	var name = req.body.name;
	var label = req.body.label;
	var dateStored = req.body.dateStored;
	var dateExp = req.body.dateExp;
	fridgeItem.create({
		name: name,
		label: label,
		dateStored: dateStored,
		dateExp: dateExp
	}, function (err, fridgeItem) {
		if (err) {
			console.log(`error creating ${fridgeItem}`);
			res.end('error!');
		}
		else {
			console.log(`${fridgeItem} created!`);
			res.end();
		}
	});
};

function itemOut(req, res) {
	var name = req.body.name;
	fridgeItem.findOneAndRemove({name: name}, function (err,doc) {
		if (err) {
			res.json({message: "woops!"});
		}
		else if (doc) {
			res.json({message: `removed ${doc}`});
		}
		else
			res.json({message: "Couldn't find one"});
	})
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
	var label = req.body.label;
	console.log("get a count for label: " + label);
	fridgeItem.count({label: label}, function (err,count) {
		if (err)
			res.json({message: "woops!"});
		else {
			res.json({count: count});
			console.log(`count = ${count}`);
		}

	});
}

function getAllByLabel(req, res) {
	var label = req.body.label;
	console.log(`get all for label: ${label}`);
	fridgeItem.find({label: label}, function (err, items) {
		if (err)
			res.json({message: "woops!"});
		else if (items) {
			console.log(`items were found ${items}`);
			res.json(items);
		}
		else
			res.json({message: "none"});
	});
}

function getAll(req, res) {
	fridgeItem.find({}, function (err, items) {
		if (err) {
			res.json({message: "woops!"});
		}
		else if (items) {
			console.log(`all items were found ${items}`);
			res.json(items);
		}
	});
}