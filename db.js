var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/searchengine');

var carSchema = new mongoose.Schema({
    model: String,
    year : String,
    state : String,
    price : String,
    tags: [String],
    url: String
}, { collection: 'cars' }
);

module.exports = { Mongoose: mongoose, CarSchema: carSchema }