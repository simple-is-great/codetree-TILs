const fs = require('fs');
let [a, b] = fs.readFileSync(0).toString().split(" ").map((num) => Number(num));

console.log(a + b);
console.log(a - b);
console.log(parseInt(a / b));
console.log(a % b);