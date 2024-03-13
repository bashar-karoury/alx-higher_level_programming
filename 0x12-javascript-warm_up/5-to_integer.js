#!/usr/bin/node
const { argv } = require('node:process');
if (Number.isInteger(Number(argv[2]))) console.log(`My number: ${Number(argv[2])}`);
else console.log('Not a number');
