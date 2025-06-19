const express = require('express');
const path = require('path');
const bodyParser = require('express').urlencoded({ extended: false });

const dpController = require("./controllers/dpController");
const dpbtController = require('./controllers/dpbtController');

const app = express();
const PORT = 3000;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.get('/', (_, res) => {
  res.render('index');
});

app.post('/dp', bodyParser, dpController.process);
app.post('/dpbt', bodyParser, dpbtController.process);

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
