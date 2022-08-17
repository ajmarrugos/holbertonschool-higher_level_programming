#!/usr/bin/node
const Square1 = require('./4-rectangle');

class Square extends Square1 {
  charPrint (c = 'X') {
    for (let s = 0; s < this.width; s++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
