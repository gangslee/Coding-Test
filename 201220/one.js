function solution(paper) {
  paper.sort((a, b) => b - a);
  for (let i = paper.length; i > 0; i--) {
    const result = paper.reduce((sum, currValue) => sum + currValue, 0);
    if (result >= i ** 2) {
      return i;
    }
    paper.pop();
  }
  return 0;
}

paper = [3, 0, 3, 0, 3, 0];

console.log(solution(paper));
