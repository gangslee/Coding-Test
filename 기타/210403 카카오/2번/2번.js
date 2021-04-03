function solution(needs, r) {
  const robot = new Array(r + 1).fill(0);

  for (let parts of needs) {
    for (let i = 0; i < parts.length; i++) {
      if (parts[i] === 1) {
        robot[i] += 1;
      }
    }
  } // needs를 다 돌면서 index별 부품 수요조사

  robot.sort((a, b) => {
    return b - a;
  });
  // 오름차순 정렬 후 r-1인덱스 (r번째로 많이 필요한 부품 개수)

  return robot[r - 1];
}

ne = [
  [1, 0, 0],
  [1, 1, 0],
  [1, 1, 0],
  [1, 0, 1],
  [1, 1, 0],
  [0, 1, 1],
];
rr = 2;
console.log(solution(ne, rr));
