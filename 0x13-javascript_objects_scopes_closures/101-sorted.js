#!/usr/bin/node

const objectToSort = require('./101-data').dict;
const newDict = Object.entries(objectToSort).reduce((acc, current) => {
  acc[current[1]] = (acc[current[1]] || []).concat(current[0]);
  return acc;
}, {});
console.log(newDict);
