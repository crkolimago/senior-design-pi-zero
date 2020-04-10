var express = require('express');
var router = express.Router();
var fs = require('fs');
const {spawn} = require('child_process');
var python;

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});


router.get('/start', (req, res, next) => {
  try {
    console.log('Starting a Trip!');
    python = spawn('python3', ['~/senior-design-pi-zero/python/script.py']);
    python.stdout.on('data', function (data) {
      console.log(data.toString());
    });
     python.on('close', (code, signal) => {
      console.log(
        `child process terminated due to receipt of signal ${signal}`);
    });
    res.sendStatus(200);  
  } catch (error) {
    console.log(error);
    res.sendStatus(404);
  }
});

router.get('/end', (req, res, next) => {
  console.log('Stopping a Trip!');
  python.kill('SIGTERM');
  try {
    res.sendStatus(200);
  } catch (error) {
    console.log(error);
    res.sendStatus(404);
  }
  
});

module.exports = router;
