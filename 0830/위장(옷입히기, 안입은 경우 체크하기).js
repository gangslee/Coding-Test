function solution(clothes) {
  const obj = {};

  clothes.map((data) => (obj[data[1]] !== undefined ? obj[data[1]]++ : (obj[data[1]] = 1)));

  let answer = 1;

  for (let i in obj) {
    answer *= obj[i] + 1;
  }
  return answer - 1;
}
