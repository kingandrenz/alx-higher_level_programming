#!/usr/bin/node

const args = process.argv.slice(2);
const num = Number(args[0]);

if (num) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
