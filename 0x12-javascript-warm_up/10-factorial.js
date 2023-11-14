#!/usr/bin/node
/*
  a script that computes and prints a factorial
*/
const computeFactorial = (n) => {
  if (isNaN(n) || n < 0) {
    return (1);
  }

  if (n === 0) {
    return (1);
  }

  return (n * computeFactorial(n - 1));
};

const arg = parseInt(process.argv[2]);
const result = computeFactorial(arg);

console.log(result);
