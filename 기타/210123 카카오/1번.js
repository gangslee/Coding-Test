function solution(n, record) {
  const server = Array.from(Array(n + 1), () => new Array());

  for (let i of record) {
    const info = i.split(' ');

    if (server[info[0]].includes(info[1])) {
      continue;
    }

    if (server[info[0]].length === 5) {
      server[info[0]].shift();
    }

    server[info[0]].push(info[1]);
  }

  let result = server[1];

  for (let i = 2; i <= n; i++) {
    result = result.concat(server[i]);
  }

  return result;
}

const n = 4;
const record = [
  '1 a',
  '1 b',
  '1 abc',
  '3 b',
  '3 a',
  '1 abcd',
  '1 abc',
  '1 aaa',
  '1 a',
  '1 z',
  '1 q',
  '3 k',
  '3 q',
  '3 z',
  '3 m',
  '3 b',
];

console.log(solution(n, record));
