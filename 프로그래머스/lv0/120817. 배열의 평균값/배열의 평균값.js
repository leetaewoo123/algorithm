function solution(numbers) {
    var answer = numbers.reduce(function add(sum, currValue){
        return sum+currValue;
    });
    return answer/numbers.length
}