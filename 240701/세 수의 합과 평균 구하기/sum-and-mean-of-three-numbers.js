const fs = require('fs');
let [a,b,c] = fs.readFileSync(0).toString().split(' ').map((n) => (Number(n)));
let sum = a + b + c;

console.log(sum);
console.log(Math.floor(sum/3));