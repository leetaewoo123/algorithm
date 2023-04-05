function solution(money) {
    var answer = [];
    answer.push(parseInt(money/5500));
    answer.push(money-parseInt(money/5500)*5500)
    return answer;
}