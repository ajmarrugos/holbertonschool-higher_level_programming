#!/usr/bin/node

/* Script that computes the number of tasks completed by user id */

const axios = require('axios').default;
const url = process.argv[2];

axios.get(url)
  .then(function (response) {
    const count = {};
    for (let i = 0; response.data[i]; i++) {
      if (response.data[i].completed === true) {
        if (isNaN(count[response.data[i].userId])) {
          count[response.data[i].userId] = 1;
        } else {
          count[response.data[i].userId] += 1;
        }
      }
    }
    console.log(count);
  });
