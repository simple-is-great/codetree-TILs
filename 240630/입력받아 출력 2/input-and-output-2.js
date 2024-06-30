const fs = require("fs");
let ssn = fs.readFileSync(0).toString().split("-");

console.log(ssn[0] + ssn[1]);