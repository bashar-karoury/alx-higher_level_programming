#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const tasks = JSON.parse(body);
    const usersTasks = {};
    for (const task of tasks) {
      if (task.completed) {
        if (usersTasks[task.userId]) {
          usersTasks[task.userId]++;
        } else {
          usersTasks[task.userId] = 1;
        }
      }
    }
    console.log(usersTasks);
  }
});
