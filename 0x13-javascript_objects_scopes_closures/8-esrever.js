#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  for (let x = 0; x < list.length; x++) reversed.unshift(list[x]);
  return reversed;
};
