function solution(n, passenger, train) {
  const graph = Array.from(Array(n + 1), () => new Array());
  const visit = Array.from(Array(n + 1), () => new Array(n + 1).fill(false));
  const result = new Array(n + 1).fill(0);

  for (let t of train) {
    graph[t[0]].push(t[1]);
    graph[t[1]].push(t[0]);
  }

  for (let i = 2; i <= n; i++) {
    dfs(1, i, 0);
  }

  function dfs(now, end, current) {
    if (visit[end][now]) {
      return;
    }

    visit[end][now] = true;

    if (graph[now].includes(end)) {
      result[end] = Math.max(current + passenger[now - 1] + passenger[end - 1], result[end]);
      return;
    }

    for (let idx = 0; idx < graph[now].length; idx++) {
      if (visit[end][graph[now][idx]] === false) {
        dfs(graph[now][idx], end, current + passenger[now - 1]);
        visit[end][graph[now][idx]] = false;
      }
    }
  }

  const answer = [-1, -1];

  for (let i = 2; i <= n; i++) {
    if (result[i] >= answer[1]) {
      answer[0] = i;
      answer[1] = result[i];
    }
  }

  return answer;
}

const nn = 6;
const passe = [1, 1, 1, 1, 1, 1];
const tra = [
  [1, 2],
  [1, 3],
  [1, 4],
  [3, 5],
  [3, 6],
];

console.log(solution(nn, passe, tra));
