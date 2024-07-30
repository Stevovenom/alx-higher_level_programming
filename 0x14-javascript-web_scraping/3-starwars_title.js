#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command-line argument
const movieId = process.argv[2];

// Define the URL for the Star Wars API
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a GET request to the URL
request(url, (error, response, body) => {
  if (error) {
    // Print the error if one occurs
    console.error(error);
  } else if (response.statusCode === 200) {
    // Parse the JSON response
    const film = JSON.parse(body);
    // Print the title of the movie
    console.log(film.title);
  } else {
    // Print an error message if the status code is not 200
    console.error(`Error: ${response.statusCode}`);
  }
});
