const express = require('express');
const path = require('path');
const bodyParser = require('express').urlencoded({ extended: false });

const app = express();
const PORT = 3000;

const lcsController = require('./controllers/lcsController');

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use('/public', express.static(path.join(__dirname, 'public')));

app.get('/', (_, res) => {
  res.render('index');
});

app.post('/result', bodyParser, lcsController.processLCS);

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
