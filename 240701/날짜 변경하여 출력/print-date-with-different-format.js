const fs = require('fs');
let dateInfo = fs.readFileSync(0).toString().split('.');
let yyyy = dateInfo[0];
let mm = dateInfo[1];
let dd = dateInfo[2];

console.log(`${mm}-${dd}-${yyyy}`);