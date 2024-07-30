#!/usr/bin/node

const request = require('request');

// Get the API URL from the command-line argument
const apiUrl = process.argv[2];

// Define the character ID for Wedge Antilles
const wedgeAntillesId = 18;

// Make a GET request to the API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    // Print the error if one occurs
    console.error(error);
  } else if (response.statusCode === 200) {
    // Parse the JSON response
    const data = JSON.parse(body);
    // Initialize a counter for the number of movies featuring Wedge Antilles
    let count = 0;

    // Loop through each film
    data.results.forEach(film => {
      // Check if Wedge Antilles is in the film's characters list
      if (film.characters.some(character => character.endsWith(`/${wedgeAntillesId}/`))) {
        count++;
      }
    });

    // Print the number of movies featuring Wedge Antilles
    console.log(count);
  } else {
    // Print an error message if the status code is not 200
    console.error(`Error: ${response.statusCode}`);
  }
});
