#!/usr/bin/node

const args = process.argv.slice(2);

if (args === null) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  const num = args.map(Number).sort((a, b) => b - a);
  console.log(num[1]);
}
