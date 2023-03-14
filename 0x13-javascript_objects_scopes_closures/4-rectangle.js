#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (x) {
    let display = '';
    let c;
    if (x) {
      c = x;
    } else {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      display += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(display);
    }
  }

  rotate () {
    const x = this.height;
    this.height = this.width;
    this.width = x;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
