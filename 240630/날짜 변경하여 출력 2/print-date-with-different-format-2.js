const fs = require("fs");
let dateInfo = fs.readFileSync(0).toString().trim().split("-"); // order: mm, dd, yyyy
let mm = dateInfo[0];
let dd = dateInfo[1];
let yyyy = dateInfo[2];

console.log(yyyy + "." + mm + "." + dd);