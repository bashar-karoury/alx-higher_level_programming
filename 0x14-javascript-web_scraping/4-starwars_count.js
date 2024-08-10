#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const id = 18;
request(url, function (error, response, body) {
  if (!error) {
    const data = JSON.parse(body);
    let count = 0;
    for (const result of data.results) {
      for (const character of result.characters) {
        if (character.endsWith(`/${id}/`)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
