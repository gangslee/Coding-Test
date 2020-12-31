function solution(n) {
  let result = 0;
  while (n >= 5) {
    if (n % 5 == 0) {
      return result + n / 5;
    }
    n -= 3;
    result++;
  }
  return n === 3 ? result + 1 : -1;
}

n = 22;

console.log(solution(n));

// n을 5의배수가 될때까지 3으로 계속 나누고 5의 배수가 안됬을 때 n이 3인경우 result++
