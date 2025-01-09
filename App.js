// app.js
const spawn = require('child_process').spawn;
const express = require('express');
const path = require('path');
const app = express();
const generateShotOutput = require('./App_Javascript'); // Import the function

const PORT = 3000;

// To handle JSON body data
app.use(express.json());

// Serve static files
app.use(express.static(path.join(__dirname, 'StaticFiles')));

// Serve the index.html file for root request
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html')); // Update with the path to your HTML file
});
app.get('/hello', (req, res) => {
    
    const py = spawn('/usr/bin/python3', ['Cricket_Project2.py', 6, 'North to South']);
    
    let output;
    py.stdout.on("data", (data) => {
          output += data.toString();
    });
    py.on("close", () => {                     // this differs 
        console.log(output);
        res.sendStatus(200);
    });
});
// Route to handle POST request and get the shot output
app.post('/get-shot', (req, res) => {
    const { windSpeed, windDirection } = req.body;
    
    // Call the backend logic (App_Javascript.js)
    const result = generateShotOutput(windSpeed, windDirection); // Get the result line

    // Send the result back as JSON
    res.json({ result });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});