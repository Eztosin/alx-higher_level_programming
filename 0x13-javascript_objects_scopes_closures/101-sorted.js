#!/usr/bin/node
/*
 imports a dictionary of occurrences by user id and computes
 a dictionary of user ids by occurrence.
*/

const { dict } = require('./101-data');

const newDict = {};
const userIds = Object.keys(dict);
let i = 0;

while (i < userIds.length) {
  const userId = userIds[i];
  const occurrences = dict[userId];

  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }
  newDict[occurrences].push(userId);

  i++;
}

console.log(newDict);
