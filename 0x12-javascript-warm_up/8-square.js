#!/usr/bin/node
const { argv } = require('node:process');
if (Number.isInteger(Number(argv[2]))) {
  const size = Number(argv[2]);
  for (let i = 0; i < size; i++) {
    let str = '';
    for (let j = 0; j < size; j++) {
      str = str + 'X';
    }
    console.log(str);
  }
} else console.log('Missing size');
