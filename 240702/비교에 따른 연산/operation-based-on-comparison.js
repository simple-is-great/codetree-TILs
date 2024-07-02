const fs = require('fs');
let [a, b] = fs.readFileSync(0).toString().split(' ').map(x => Number(x));
let answer;

if (a > b) {
    answer = a * b;
} else {
    answer = Math.floor(b / a);
}

console.log(answer);