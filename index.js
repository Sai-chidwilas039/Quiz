const express = require('express');
const mysql = require('mysql2');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// MySQL Connection
const connection = mysql.createConnection({
    host: 'localhost',         // Replace with your MySQL host
    user: 'root',              // Replace with your MySQL username
    password: 'password',      // Replace with your MySQL password
    database: 'quiz_app'       // Replace with your database name
});

connection.connect(err => {
    if (err) {
        console.error('Error connecting to MySQL:', err);
        return;
    }
    console.log('Connected to MySQL');
});

// Route to handle POST requests for saving quiz results
app.post('/save-results', (req, res) => {
    const { user_name, user_score, user_total } = req.body;

    if (!user_name || user_score == null || user_total == null) {
        return res.status(400).send('Missing required fields');
    }

    const query = 'INSERT INTO quiz_results (user_name, user_score, user_total) VALUES (?, ?, ?)';
    connection.query(query, [user_name, user_score, user_total], (err, result) => {
        if (err) {
            console.error('Error saving quiz results:', err);
            return res.status(500).send('Failed to save results');
        }
        res.send('Quiz results saved successfully');
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
