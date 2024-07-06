const fs = require('fs');
let numbers = new Array(9).fill(0);
let input = fs.readFileSync(0).toString().split('\n');
let n = Number(input[0]);
input = input[1].split(' ').map(Number);
// console.log(input);

for (let i = 0; i < n; i++){
    numbers[input[i] - 1] += 1;
}

for (let i = 0; i < 9; i++) {
    console.log(numbers[i]);
}