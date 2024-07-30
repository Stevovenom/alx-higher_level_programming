#!/usr/bin/node

const fs = require('fs');
const request = require('request');

// Get the URL and file path from command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the URL
request(url, (error, response, body) => {
  if (error) {
    // Print the error if one occurs
    console.error(error);
  } else if (response.statusCode === 200) {
    // Write the response body to the file
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        // Print an error if one occurs while writing to the file
        console.error(err);
      }
    });
  } else {
    // Print an error message if the status code is not 200
    console.error(`Error: ${response.statusCode}`);
  }
});
