#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const id = 18;
request(url, function (error, response, body) {
  if (!error) {
    const data = JSON.parse(body);
    let count = 0;
    const rootUrl = `${response.request.uri.protocol}//${response.request.uri.host}`;
    const character = `${rootUrl}/api/people/${id}/`;
    for (const result of data.results) {
      if (result.characters.includes(character)) {
        count++;
      }
    }
    console.log(count);
  }
});
