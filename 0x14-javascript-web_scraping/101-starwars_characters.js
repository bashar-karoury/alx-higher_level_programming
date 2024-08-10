#!/usr/bin/node
const request = require('request');
const util = require('util');
// Convert request to return a Promise
const requestPromise = util.promisify(request);
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(url, async function (error, response, body) {
  if (!error) {
    const charactersUrls = JSON.parse(body).characters;

    // Fetch character names sequentially
    for (const characterUrl of charactersUrls) {
      const { body } = await requestPromise(characterUrl);
      console.log(JSON.parse(body).name);
    }
  }
});
