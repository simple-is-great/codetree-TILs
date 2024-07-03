const fs = require('fs');
let n = Number(fs.readFileSync(0).toString().trim());
let score;

if (n >= 90) {
    score = 'A';
} else if (n >= 80) {
    score = 'B';
} else if (n >= 70) {
    score = 'C';
} else if (n >= 60) {
    score = 'D'
} else score = 'F';

console.log(score);