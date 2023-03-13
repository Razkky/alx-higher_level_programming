#!/usr/bin/node

const number = parseInt(process.argv[2]);
if (process.argv[2] === undefined || isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('MY number: ' + number);
}
