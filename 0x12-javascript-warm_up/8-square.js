#!/usr/bin/node

const args = process.argv.slice(2);
const num = Number(args[0]);

if (!num) {
  console.log('Missing size');
} else {
  const square = 'X'.repeat(num);

  for (let i = 0; i < num; i++) {
    console.log(square);
  }
}
