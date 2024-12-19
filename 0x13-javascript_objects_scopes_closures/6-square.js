#!/usr/bin/node
const SquareBase = require('./5-square');

module.exports = class Square extends SquareBase {
  charPrint(c) {
    const char = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
};
