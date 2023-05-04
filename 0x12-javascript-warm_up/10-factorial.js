#!/usr/bin/node

const args = process.argv[2];

function fact (a) {
  if (isNaN(a)) {
    return 1;
  }
  if (a === 0) {
    return 1;
  }
  return a * fact(a - 1);
}

console.log(fact(Number(args)));
