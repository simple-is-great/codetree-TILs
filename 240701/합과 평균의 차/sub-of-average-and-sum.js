const fs = require('fs');
let [a, b, c] = fs.readFileSync(0).toString().split(' ').map((n) => Number(n));
let sum = a + b + c;
let avg = sum / 3;
let diff = sum - avg;

console.log(sum);
console.log(avg);
console.log(diff);