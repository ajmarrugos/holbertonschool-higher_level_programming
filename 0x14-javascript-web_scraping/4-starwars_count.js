#!/usr/bin/node

/* Script that prints the number of movies where the character “Wedge Antilles” is present */

const axios = require('axios').default;
const args = process.argv;

axios.get(args[2])
  .then(function (response) {
    const films = response.data.results;
    const result = films.filter(function (p) {
      return p.characters.indexOf('https://swapi-api.hbtn.io/api/people/18/') > -1;
    });
    console.log(result.length);
  })
  .catch(function (error) {
    console.log(error);
  });
