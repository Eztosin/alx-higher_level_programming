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
          request(characterUrl, (err, resp, characterBody) => {
            if (err) {
              reject(new Error('Error fetching character data'));
            } else {
              if (resp.statusCode === 200) {
                const characterData = JSON.parse(characterBody);
                resolve(characterData.name);
              } else {
                reject(new Error(`Failed to retrieve character data. Status code: ${resp.statusCode}`));
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
        .catch((err) => {
          console.error('Error:', err.message);
        });
    } else {
      console.error(`Failed to retrieve movie data. Status code: ${response.statusCode}`);
    }
  }
});
