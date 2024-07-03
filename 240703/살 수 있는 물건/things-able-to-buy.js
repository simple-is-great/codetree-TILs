const fs = require('fs');
let n = Number(fs.readFileSync(0).toString().trim());
let name = 'no';

if (n >= 3000) {
    name = 'book';
} else if (n >= 1000) {
    name = 'mask';
}

console.log(name);