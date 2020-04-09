var express = require('express');
var router = express.Router();
var fs = require('fs');



/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});


router.get('/start', (req, res, next) => {
  try {
    console.log('Starting a Trip!');
    res.sendStatus(200);  
  } catch (error) {
    console.log(error);
    res.sendStatus(404);
  }
  
});

router.get('/stop', (req, res, next) => {
  console.log('Stopping a Trip!');
  try {
    res.sendStatus(200);
  } catch (error) {
    console.log(error);
    res.sendStatus(404);
  }
  
});

module.exports = router;
