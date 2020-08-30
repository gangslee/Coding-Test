const c = [
  ['yellow_hat', 'headgear'],
  ['blue_sunglasses', 'eyewear'],
  ['green_turban', 'headgear'],
];

const obj = {};

c.map((data) => (obj[data[1]] !== undefined ? obj[data[1]]++ : (obj[data[1]] = 1)));

let answer = 1;

for (let i in obj) {
  answer *= obj[i] + 1;
}

console.log(answer - 1);
