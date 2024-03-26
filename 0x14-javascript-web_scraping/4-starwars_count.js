#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, data, body) => {
  if (err) {
    console.log(err);
  } else {
    let counter = 0;
    const films = JSON.parse(body).results;
    for (let i = 0; i < films.length; i++) {
      const characters = films[i].characters;
      for (let j = 0; j < characters.length; j++) {
        const character = characters[j];
        const characterId = character.split('/')[5];

        if (characterId === '18') {
          counter += 1;
        }
      }
    }
    console.log(counter);
  }
});
