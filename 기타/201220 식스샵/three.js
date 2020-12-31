function solution(n) {
  const oneCnt = n.toString(2).match(/1/g).length;
  let result = 0;
  for (let i = 1; i < n; i++) {
    let temp = i;
    let j;
    for (j = 0; temp != 0; j++) {
      temp &= temp - 1;
    }

    if (j === oneCnt) {
      result += 1;
    }
  }
  return result;
}
