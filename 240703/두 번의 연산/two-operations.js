const fs = require('fs');
let a = Number(fs.readFileSync(0).toString().trim());
let answer = a;

if (a % 2 === 1) {
    answer += 3;
}

if (a % 3 === 0) {
    answer /= 3;
}

console.log(Math.floor(answer));