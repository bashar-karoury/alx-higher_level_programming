#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length < 4) console.log(0);
else {
  const argsNumbers = argv.slice(2, argv.length);
  argsNumbers.forEach((element, index) => {
    argsNumbers[index] = Number(element);
  });
  const argsSorted = argsNumbers.sort((a, b) => a - b);
  console.log(argsSorted[argsSorted.length - 2]);
}
