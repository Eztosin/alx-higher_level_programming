#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Please provide the Star Wars API URL as an argument.');
  process.exit(1);
}

const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    if (response.statusCode === 200) {
      const films = JSON.parse(body).results;
      let count = 0;
      films.forEach((film) => {
        if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
          count++;
        }
      });
      console.log(count);
    } else {
      console.error(`Failed to retrieve movie data. Status code: ${response.statusCode}`);
    }
  }
});
