const axios = require('axios');
const {addOrUpdateCharacters} = require('./dynamo');

const seedData = async () => {
    const url = 'https://hp-api.herokuapp.com/api/characters'
    try {
        const {data : characters} = await axios.get(url);
        const characterPromises = characters.map((character, i) => {
            addOrUpdateCharacters({... character, id: i + ''}) // add the character for that index and add an id but convert to string by concatenating with an empty string
        });
        await Promise.all(characterPromises);
    } catch (error) {
        console.log(error);
        console.log('WHOOPS!');
    }
}

seedData();