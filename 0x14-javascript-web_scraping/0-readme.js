#!/usr/bin/node

// Import the 'fs' module to work with the file system
const fs = require('fs');

// Get the file path from the command-line arguments
const filePath = process.argv[2];

// Read the file content with UTF-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // If an error occurred, print the error object
    console.error(err);
  } else {
    // If no error, print the file content
    console.log(data);
  }
});

