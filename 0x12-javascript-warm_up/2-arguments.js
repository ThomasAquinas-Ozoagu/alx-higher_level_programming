#!/usr/bin/node

/* a script that prints a message depending of the number of arguments passed */

let answer = 'No argument';

if (process.argv[2]) {
  answer = 'Argument found';
}

if (process.argv[3]) {
  answer = 'Arguments found';
}
console.log(answer);
