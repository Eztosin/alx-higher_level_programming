#!/usr/bin/node

const request = require('request');

const movieId = parseInt(process.argv[2]);

if (!movieId || isNaN(movieId)) {
  console.error('Please provide a valid movie ID as an argument.');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films`;

request(apiUrl, (error, response, body) => {
    const movieData = JSON.parse(body);
    for (let i = 1; i < movieData.results.length + 1; i++;) {
	if (i === movieId) {
	    console.log(movieData.results[i - 1].title);
	}
    }
    if (error) {
	console.error(error);
    }
});
