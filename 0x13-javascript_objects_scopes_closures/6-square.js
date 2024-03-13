#!/usr/bin/node
const SquareOld = require('./5-square');
class Square extends SquareOld {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str = str + c;
      }
      console.log(str);
    }
  }
}
module.exports = Square;
