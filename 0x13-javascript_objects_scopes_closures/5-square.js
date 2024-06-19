#!/usr/bin/node
/* inheritance in JS */
const Rectangle = require('./4-rectangle');
// call the inheritance
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
