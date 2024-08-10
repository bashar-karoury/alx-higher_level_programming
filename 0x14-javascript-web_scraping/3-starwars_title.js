#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
console.log(url);
request(url, function (error, response, body) {
  if (!error) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
