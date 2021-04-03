function solution(gift_cards, wants) {
  let answer = 0;

  for (let i = 0; i < gift_cards.length; i++) {
    for (let j = i + 1; j < gift_cards.length; j++) {
      if (gift_cards[j] === wants[i]) {
        [gift_cards[i], gift_cards[j]] = [gift_cards[j], gift_cards[i]];
        break;
      }
    }
  }

  // 앞에서부터 뒤에 번호들 중 내 wants와 일치하는게 있으면 스왑

  for (let i = 0; i < gift_cards.length; i++) {
    if (gift_cards[i] !== wants[i]) {
      answer++;
    }
  }

  // 다른 개수 세기

  return answer;
}

const gc = [4, 5, 3, 2, 1];
const wa = [2, 4, 4, 5, 1];

console.log(solution(gc, wa));
