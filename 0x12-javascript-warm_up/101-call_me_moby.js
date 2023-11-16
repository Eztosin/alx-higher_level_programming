#!/usr/bin/node
/*
a function that executes x times a function
*/
function callMeMoby (x, theFunction) {
  if (x > 0) {
    theFunction();
    callMeMoby(x - 1, theFunction);
  }
}

module.exports = { callMeMoby };
