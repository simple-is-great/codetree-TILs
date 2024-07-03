const fs = require('fs');
let a = Number(fs.readFileSync(0).toString().trim());
let status;

if (a >= 1.0) {
    status = "High";
} else if (a >= 0.5) {
    status = "Middle";
} else {
    status = "Low";
}

console.log(status);