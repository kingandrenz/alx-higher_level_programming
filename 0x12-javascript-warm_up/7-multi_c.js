#!/usr/bin/node

const args = process.argv.splice(2);
const C = 'C is fun';
const x = Number(args[0]);

if (!x) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log(C);
  }
}
