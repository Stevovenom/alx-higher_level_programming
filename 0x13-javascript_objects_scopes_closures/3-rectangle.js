#!/usr/bin/node
/* create an rectangle class in JS */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Method
  print () {
    let row = '';
    let count = 0;
    // we create the first row depending of width
    for (; count < this.width; count++) {
      row = row + 'X';
    }
    count = 0;
    // print the row created height times
    for (; count < this.height; count++) {
      console.log(row);
    }
  }
};
