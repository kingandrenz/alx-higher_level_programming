#!/usr/bin/node

const args = process.argv.splice(2);
const C = 'c is fun';
const num = Number(args[0]);

if (!num) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log(C);
  }
}
