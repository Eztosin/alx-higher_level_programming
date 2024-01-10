#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const text_file = process.argv[3]

fs.writeFile(filePath, text_file, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
