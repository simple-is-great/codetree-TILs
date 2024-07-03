const fs = require('fs');
let [a, b] = fs.readFileSync(0).toString().split(' ');
let answerA;

if (Number(a) < Number(b)){
    answerA = 1;
} else {
    answerA = 0;
}

let answerB;

if (Number(a) === Number(b)){
    answerB = 1;
} else {
    answerB = 0;
}

console.log(answerA, answerB);