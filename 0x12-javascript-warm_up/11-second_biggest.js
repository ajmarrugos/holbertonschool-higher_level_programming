#!/usr/bin/node
function secondBiggest (numbers) {
    if (numbers.length <= 3) return 0;
  
    numbers.sort(function (a, b) {
      return b - a;
    });
    return numbers[3];
  }
  console.log(secondBiggest(process.argv));
  