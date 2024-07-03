const fs = require('fs');
let n = Number(fs.readFileSync(0).toString().trim());
let result = 'no';

if (n >= 3000){
    result = 'book';
} else if (n >= 1000) {
    result = 'mask';
} else if (n >= 500) {
    result = 'pen';
}

console.log(result);