#!/usr/bin/node

/* a script that prints a message depending of the number of arguments passed */

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
