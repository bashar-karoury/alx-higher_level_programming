#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const id = 18;
const character = `http://swapi.co/api/people/${id}/`;
request(url, function (error, response, body) {
  if (!error) {
    const data = JSON.parse(body);
    let count = 0;

    for (const result of data.results) {
      if (result.characters.includes(character)) {
        count++;
      }
    }
    console.log(count);
  }
});
