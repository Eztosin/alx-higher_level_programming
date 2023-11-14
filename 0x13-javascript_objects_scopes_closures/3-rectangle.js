#!/usr/bin/node
/*
a class Rectangle that defines a rectangle
*/

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      let i = 0;
      while (i < this.height) {
        console.log('X'.repeat(this.width));
        i++;
      }
    }
  }
}

module.exports = Rectangle;
