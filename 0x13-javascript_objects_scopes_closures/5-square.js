#!/usr/bin/node

const Rectangle = require('./4-rectangle');
const square = class square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
module.exports = square;
