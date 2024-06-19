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
    for (; count < this.width; count++) {
      row = row + 'X';
    }
    count = 0;
    for (; count < this.height; count++) {
      console.log(row);
    }
  }

  rotate () {
    let aux = 0;
    aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
