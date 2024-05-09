#!/usr/bin/node

/* a script that prints x times “C is fun” */

const arg1 = Number(process.argv[2]);
const roww = 'x';

if (isNaN(arg1)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg1; i++) {
    console.log(`${roww.repeat(arg1)}`);
  }
}
