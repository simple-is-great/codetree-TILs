const fs = require('fs');
const charArr = ['L', 'E', 'B', 'R', 'O', 'S'];
let idx = -1;

let toFind = fs.readFileSync(0).toString().trim();

for (let i = 0; i < 6; i++) {
    if (charArr[i] === toFind) {
        idx = i;
    }
}

console.log(idx === -1 ? "None" : idx);