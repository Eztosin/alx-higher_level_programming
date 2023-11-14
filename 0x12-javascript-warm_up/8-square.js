#!/usr/bin/node
/*
  a script that prints a square
*/
const squareSize = parseInt(process.argv[2]);

if (!isNaN(squareSize) && squareSize > 0) {
  let i = 0;
  while (i < squareSize) {
    let row = '';
    let j = 0;
    while (j < squareSize) {
      row += 'X';
      j++;
    }
    console.log(row);
    i++;
  }
} else {
  console.log('Missing size');
}
