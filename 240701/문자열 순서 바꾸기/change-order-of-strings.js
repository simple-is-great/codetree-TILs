const fs = require('fs');
let [s, t] = fs.readFileSync(0).toString().split('\n');

console.log(t);
console.log(s);