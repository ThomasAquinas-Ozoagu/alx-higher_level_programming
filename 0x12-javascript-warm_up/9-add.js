#!/usr/bin/node

/* a script that prints x times “C is fun” */

const arg1 = Number(process.argv[2]);
const arg2 = Number(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(arg1, arg2));
