#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId || isNaN(movieId)) {
  console.error('Please provide a valid Movie ID as an argument.');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const characters = movieData.characters;
      
      const promises = characters.map((characterUrl) => {
        return new Promise((resolve, reject) => {
          request(characterUrl, (error, response, body) => {
            if (error) {
              reject(error);
            } else {
              if (response.statusCode === 200) {
                const characterData = JSON.parse(body);
                resolve(characterData.name);
              } else {
                reject(`${response.statusCode}`);
              }
            }
          });
        });
      });

      Promise.all(promises)
        .then((characterNames) => {
          characterNames.forEach((name) => {
            console.log(name);
          });
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    } else {
      console.error(`Status code: ${response.statusCode}`);
    }
  }
});
