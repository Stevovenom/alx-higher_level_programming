#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./101-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  // Parse the JSON response
  const film = JSON.parse(body);

  if (!film || !film.characters) {
    console.error('Error: No characters found for this movie.');
    process.exit(1);
  }

  // Fetch all character URLs
  const characters = film.characters;

  // Function to fetch and print character names in order
  function fetchCharacter (index) {
    if (index >= characters.length) {
      return;
    }

    request(characters[index], (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        process.exit(1);
      }

      const character = JSON.parse(body);
      console.log(character.name);

      // Fetch the next character
      fetchCharacter(index + 1);
    });
  }

  // Start fetching characters
  fetchCharacter(0);
});
