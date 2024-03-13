#!/usr/bin/node
const { argv } = require('node:process');

function factorial (a) {
  if ((isNaN)(a) || a === undefined) return 1;
  if (a === 1) return 1;
  return (a * factorial(a - 1));
}
const n1 = Number(argv[2]);
console.log(factorial(n1));
