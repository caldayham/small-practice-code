const express = require('express');
const { 
    getCharacters,
    getCharacterById,
    addOrUpdateCharacters,
    dynamoClient,
    deleteCharacterById,
 } = require('./dynamo');
const app = express();

app.use(express.json());

app.get('/', (req, res) => {
    res.send('Hello World');
});

app.get('/characters', async (req, res) => {
    try {
        const characters = await getCharacters();
        res.json(characters);
    } catch (error) {
        console.error(err);
        res.status(500).json({ err: 'big whoops'});
    }
});

app.get('/characters/:id', async (req, res) => {
    const id = req.params.id;
    try {
        const characters = await getCharacterById(id);
        res.json(characters);
    } catch (error) {
        console.error(err);
        res.status(500).json({ err: 'big whoops'});
    }
});

app.post('/characters', async (req, res) => {
    const character = req.body;
    try {
        const newCharacter = await addOrUpdateCharacters(character);
        res.json(newCharacter);
    } catch (error) {
        console.error(err);
        res.status(500).json({ err: 'big whoops'});
    }
});

app.put('/characters/:id', async (req, res) => {
    const character = req.body;
    const { id } = req.params;
    character.id = id;
    try {
        const updatedCharacter = await addOrUpdateCharacters(character);
        res.json(updatedCharacter);
    } catch (error) {
        console.error(err);
        res.status(500).json({ err: 'big whoops'});
    }
});

app.delete('/characters/:id', async (req, res) => {
    const { id } = req.params;
    try {
        res.json(await deleteCharacterById(id));
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'big whoops'});
    }
});

const port = process.env.PORT || 3000;

app.listen(port, () => {
    console.log(`listening on port ${process.env.PORT || "3000"}`)
});