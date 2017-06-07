var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { results: false });
});

/* GET search page. */
router.get('/search', function (req, res, next) {
    var searchParams = req.query.query.toUpperCase().split(' ');
   
    // search = {'a' : searchParams[0], 'b' : searchParams[1], 'c' : searchParams[2]}
    search = {'a' : req.query.model, 'b' : req.query.year, 'c' : req.query.state}
    
    if(searchParams[0] != '')
        searchParams.push(search['a']);
    else
        searchParams = [search['a']];

    console.log('DATA: ',search);
    console.log('SearchParams: ', searchParams);

    var spawn = require('child_process').spawn,
        py = spawn('python', ['naivebayes.py']),
        data = [search],
        classify = '';

        py.stdout.on('data', function(data){
        classify = data.toString();
        });

        py.stdout.on('end', function(){
        console.log('Dados recebidos: ', classify)
        });

        py.stdin.write(JSON.stringify(data));
        py.stdin.end();

    var accuracy = '';

    function price_definition() {
    //Definição das faixas de preço, dependentes da classificação da busca
        if(classify[3] === 'A'){
            low_price = '02.000'
            high_price = '15.000'
            accuracy = classify[9]+classify[10]+classify[11]+classify[12]+classify[13]
        }
        else if(classify[3] === 'B'){
            low_price = '15.000'
            high_price = '30.000'
            accuracy = classify[18]+classify[19]+classify[20]+classify[21]+classify[22]
        }
        else if(classify[3] === 'C'){
            low_price = '30.000'
            high_price = '99.000'
            accuracy = classify[27]+classify[28]+classify[29]+classify[30]+classify[31]
        }
        console.log('Faixa de preço recomendada: ', low_price, ' - ', high_price)
        console.log('Probabilidade de estar na faixa correta: ', accuracy)
    }

    low_price = '02.000'
    high_price = '99.000'

    function mongo_query() {
        var db = require('../db');
        var Car = db.Mongoose.model('cars', db.CarSchema, 'cars');
    Car.find( {$and: [ {price: {$gt : low_price, $lt : high_price}}, {year: {$gt : search['b']}}, {location : search['c']}, {tags : { $all: searchParams } }]}, function (e, docs) {
            res.render('index', { results: true, search: search['a'], list: docs });
        });
    }

    setTimeout(price_definition, 2000);
    setTimeout(mongo_query, 4000);
});

module.exports = router;
