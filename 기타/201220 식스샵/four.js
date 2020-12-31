function solution(foods) {
  let avg = foods.reduce((sum, currValue) => sum + currValue, 0);
  if (avg % 3 !== 0) {
    return 0;
  } else {
    avg /= 3;
  }

  let sum = 0;
  let start = 0;
  let end = foods.length - 1;

  for (start; start < foods.length; start++) {
    sum += foods[start];
    if (sum === avg) {
      break;
    }
  }

  for (end; end >= start; end--) {
    sum += foods[end];
    if (sum === avg * 2) {
      break;
    }
  }

  if (start === end) {
    return 0;
  } else {
    sum = 0;
  }

  foods = foods.slice(start + 1, end);

  let cntValue = 0;
  let multiple = 1;
  let result = 1;

  for (let i = 0; i < foods.length; i++) {
    sum += foods[i];

    if (sum === cntValue) {
      multiple++;
    }

    if (sum === avg && cntValue === 0 && avg !== 0) {
      cntValue = avg;
      result *= multiple;
      multiple = 1;
    }
  }

  return result * multiple;
}

foods = [0, 0, 0, 0];

console.log(solution(foods));
