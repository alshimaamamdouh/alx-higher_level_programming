#!/usr/bin/node

const request = require('request');
const finalUrl = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(finalUrl, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
