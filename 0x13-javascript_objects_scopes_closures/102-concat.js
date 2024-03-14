#!/usr/bin/node
const { argv } = require('node:process');
const fs = require('fs');
if (argv.length === 5) {
  const f1 = argv[2];
  const f2 = argv[3];
  const f3 = argv[4];
  // read first file and write it to the third
  const data1 = fs.readFileSync(f1, 'utf8');
  // read second file and write it to the third
  const data2 = fs.readFileSync(f2, 'utf8');
  fs.appendFileSync(f3, data1);
  fs.appendFileSync(f3, data2);
}
