#!/usr/bin/node
/*
a function that increments and calls a function
*/

function addMeMaybe (number, theFunction) {
  theFunction(number + 1);
}

module.exports = { addMeMaybe };
