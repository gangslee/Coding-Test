function solution(n, s, a, b, fares) {
  var answer = 0;
  const d = Array.from(Array(n + 1), () => new Array(n + 1));
  fares.map((f) => {
    d[f[0]][f[1]] = f[2];
    d[f[1]][f[0]] = f[2];
  });

  const findLoad = (start, arrive) => {
    const visit = [start];
    while (arrive !== visit[visit.length - 1]) {
      visit.push(Math.min.apply(null, d[visit[visit.length - 1]]));
      console.log(visit[visit.length - 1]);
    }
    console.log(visit);
  };

  findLoad(s, a);

  return answer;
}

const n = 6;
const s = 4;
const a = 6;
const b = 2;
const f = [
  [4, 1, 10],
  [3, 5, 24],
  [5, 6, 2],
  [3, 1, 41],
  [5, 1, 24],
  [4, 6, 50],
  [2, 4, 66],
  [2, 3, 22],
  [1, 6, 25],
];

console.log(solution(n, s, a, b, f));
