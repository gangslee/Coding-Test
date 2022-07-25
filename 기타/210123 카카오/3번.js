function solution(next_student) {
  next_student.unshift(0);
  const visit = Array.from(Array(next_student.length), () =>
    new Array(next_student.length).fill(false)
  );
  const result = new Array(next_student.length).fill(0);

  const dfs = (current, n) => {
    if (visit[current][n]) {
      return;
    }

    visit[current][n] = true;
    result[current] += 1;

    if (next_student[n] !== 0) {
      dfs(current, next_student[n]);
    }
  };

  for (let i = 1; i < next_student.length; i++) {
    dfs(i, i);
  }

  return result.lastIndexOf(Math.max(...result));
}

const next_student = [5, 9, 13, 1, 0, 0, 11, 1, 7, 12, 9, 9, 2];
console.log(solution(next_student));
