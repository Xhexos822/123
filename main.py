const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();
const port = 3000;

app.use(bodyParser.json());

// Endpoint to check key
app.post('/check_key', (req, res) => {
    const { key } = req.body;
    if (!key) {
        return res.status(400).json({ error: 'Key is required' });
    }

    // Load keys from JSON file
    fs.readFile('keys.json', 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading file:', err);
            return res.status(500).json({ error: 'Internal server error' });
        }

        const keys = JSON.parse(data);
        if (keys.includes(key)) {
            return res.status(200).json({ valid: true });
        } else {
            return res.status(200).json({ valid: false });
        }
    });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
