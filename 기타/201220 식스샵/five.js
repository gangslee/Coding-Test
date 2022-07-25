function solution(n, relation) {
  const graph = Array.from(Array(n + 1), () => new Array());

  for (let line of relation) {
    graph[line[0]].push(line[1]);
    graph[line[1]].push(line[0]);
  }

  const result = [];

  for (let i = 1; i <= n; i++) {
    let friend = graph[i].map((n) => n);
    // map으로 한 이유 friend = graph[i] 일 경우 friend 내부의 값을 변경할 시 원본도 그대로 복사되서 새로운 map을 통해 동일한 새로운 list를 생성
    let maxIdx = friend.length;

    for (let j = 0; j < maxIdx; j++) {
      friend.push(...graph[friend[j]]);
    }
    friend = new Set(friend);
    friend.delete(i);
    result.push(friend.size);
  }

  return result;
}

relation = [
  [1, 2],
  [4, 2],
  [3, 1],
  [4, 5],
];

console.log(solution(5, relation));

// 그래프를 그리고 해당 인덱스 array를 friend에 담고 friend의 인덱스를 다 돌면서 friend에 넣어주고 set(집합)으로 중복 제거, 본인 제거 실시
