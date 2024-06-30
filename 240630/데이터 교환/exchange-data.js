let [a, b, c] = [5, 6, 7];
let temp = c;
c = b;
b = a;
a = temp;

console.log(a);
console.log(b);
console.log(c);