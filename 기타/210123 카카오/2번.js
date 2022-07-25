function solution(m, v) {
  const result = new Array();

  for (let block of v) {
    result.unshift(0);

    for (let i = 0; i < result.length; i++) {
      if (block + result[i] > m) {
        result[i - 1] += block;
        if (i !== 1) {
          result.shift();
        }
        break;
      }

      if (i === result.length - 1) {
        result[i] += block;
        if (i !== 0) {
          result.shift();
        }
      }
    }
  }

  return result.length;
}

const m = 4;
const v = [2, 3, 1];

console.log(solution(m, v));
