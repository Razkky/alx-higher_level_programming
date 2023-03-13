#!/usr/bin/node

let x = parseInt(process.argv[2]);
let myVar = '';
if (process.argv[2] === undefined || isNaN(x)) {
  console.log('Missing size');
} else {
  while (x > 0) {
    myVar += 'X';
    x--;
  }
  x = parseInt(process.argv[2]);
  while (x > 0) {
    console.log(myVar);
    x--;
  }
}
