const fs = require('fs');
let n = fs.readFileSync(0).toString().trim();
let result;

if (n === 'S'){
    result = 'Superior';
} else if (n === 'A') {
    result = 'Excellent';
} else if (n === 'B') {
    result = 'Good';
} else if (n === 'C') {
    result = 'Usually';
} else if (n === 'D') {
    result = 'Effort';
} else result = 'Failure';

console.log(result);