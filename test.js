function solution(n, relation) {
  const graph = Array.from(Array(n + 1), () => new Array());

  for (let line of relation) {
    graph[line[0]].push(line[1]);
    graph[line[1]].push(line[0]);
  }

  const result = [];

  for (let i = 1; i <= n; i++) {
    let friend = graph[i].map((n) => n);
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
