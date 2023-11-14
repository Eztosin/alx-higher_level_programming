#!/usr/bin/node
/*
a class square that defines a square and inherits from
Rectangle of 5-square.js:
*/

const Square = require('./5-square');

class SquareWithCharPrint extends Square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    const line = c.repeat(this.width);
    let i = 0;
    while (i < this.height) {
      console.log(line);
      i++;
    }
  }
}
module.exports = SquareWithCharPrint;
