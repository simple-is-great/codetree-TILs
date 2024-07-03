const fs = require('fs');
let T = Number(fs.readFileSync(0).toString().trim());
let status;

if (T < 0) {
    status = "ice";
} else if (T >= 100) {
    status = "vapor";
} else {
    status = "water";
}

console.log(status);