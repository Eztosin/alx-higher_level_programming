#!/usr/bin/node
/*
concats 2 files
*/

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const textsA = fs.readFileSync(fileA, 'utf8');
const textsB = fs.readFileSync(fileB, 'utf8');
const concatenatedTexts = textsA + textsB;

fs.writeFileSync(fileC, concatenatedTexts);
