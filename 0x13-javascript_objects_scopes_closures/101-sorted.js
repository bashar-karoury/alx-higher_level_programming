#!/usr/bin/node
const dict = require('./101-data').dict;
const newdict = {};
for (const key in dict) {
  const val = dict[key];
  newdict[val] = [];
  Object.entries(dict).forEach(([k, v]) => {
    if (dict[k] === val) {
      newdict[val].push(k);
    }
  });
}
console.log(newdict);
