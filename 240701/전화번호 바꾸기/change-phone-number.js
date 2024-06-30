const fs = require('fs');
let phoneNumber = fs.readFileSync(0).toString().split('-');
let prefix = phoneNumber[0];
let xxxx = phoneNumber[1];
let yyyy = phoneNumber[2];

console.log(`${prefix}-${yyyy}-${xxxx}`);