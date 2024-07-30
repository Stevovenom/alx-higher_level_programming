#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./100-starwars_characters.js <Movie ID>');
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

  // Fetch each character's name
  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        process.exit(1);
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
