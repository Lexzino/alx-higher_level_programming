#!/usr/bin/node
const firstSquare = require('./5-square');

class Square extends firstSquare {
  charPrint (c) {
    const character = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      let y = 0;
      while (y < this.width) {
        myVar += character;
        y++;
      }
      console.log(myVar);
    }
  }
}

module.exports = Square;
