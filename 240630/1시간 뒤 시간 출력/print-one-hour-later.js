const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(":");
let h = Number(input[0]);
let m = input[1];

console.log((h+1).toString()+":"+m);