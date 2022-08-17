#!/usr/bin/node
function factorialize (num) {
    if (num === 0 || isNaN(num)) {
      return 1;
    }
    return num * factorialize(num - 1);
  }
  const x = parseInt(process.argv[2]);
  console.log(factorialize(x));
  