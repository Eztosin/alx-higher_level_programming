#!/usr/bin/node
/*
 a script that that searches the second biggest integer in
 the list of arguments
*/
const args = process.argv.slice(2).map(arg => parseInt(arg, 10));

const findSecondLargest = (arr) => {
  if (arr.length <= 1) {
    return 0;
  }

  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (const num of arr) {
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num !== largest) {
      secondLargest = num;
    }
  }

  return secondLargest;
};
console.log(findSecondLargest(args));
