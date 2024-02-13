#!/usr/bin/node
const square = require('./5-square.js');
class Square extends square {
  charPrint (c) {
    let sympol = '';
    if (c === undefined) {
      sympol = 'X';
    } else {
      sympol = 'c';
    }
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += sympol;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
