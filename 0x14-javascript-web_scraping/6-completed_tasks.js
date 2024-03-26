#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const userId = 0;
condst printed = {}

request(url, (err, res, body) => {
	if(err) {
		console.error(err);
	} else {
		const response = JSON.parse(body);
		for (let i = 0; i < response.length; i++) {
			if (response[i].completed) {


			}
		}

	}
)};
