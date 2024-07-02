const fs = require('fs');
let testScore = Number(fs.readFileSync(0).toString().trim());

console.log(testScore === 100 ? 'pass': 'failure');