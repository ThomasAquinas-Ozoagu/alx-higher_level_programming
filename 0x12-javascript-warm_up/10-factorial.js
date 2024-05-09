#!/usr/bin/node

/* a script that computes and prints a factorial */

const arg1 = Number(process.argv[2]);

function facto (a) {
    if (a > 1) {
    return (a * facto(a - 1));
  } else {
      return 1;
  }
}

console.log(facto(arg1))
