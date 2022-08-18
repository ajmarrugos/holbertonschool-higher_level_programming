#!/usr/bin/node

/* Script that writes content to a file */

const fs = require('fs');
const arg = process.argv.slice(2);

fs.writeFile(arg[0], arg[1], err => {
  if (err) {
    console.error(err);
  }
});
