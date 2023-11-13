#!/usr/bin/node

/*
 a script that prints the first argument passed to it
*/

const argv = process.argv.slice(2);
if (argv.length === 0) {
  console.log('No argument');
} else if (argv.length === 1) {
  console.log(argv[0]);
}
