#!/usr/bin/node

const square_ = require('./5-square');
const square = class square extends square_ {
  charPrint (c) {
    if (c) {
      let prints = '';
      for (let t = 0; t < this.height; t++) {
        for (let t = 0; t < this.height; t++) {
          prints += c;
        }
        console.log(prints);
        prints = '';
      }
    } else {
      super.print();
    }
  }
};
module.exports = square;
