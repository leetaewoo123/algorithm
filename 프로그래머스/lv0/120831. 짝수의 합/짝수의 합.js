function solution(n) {
    var answer = 0;
    for (n; n>0; n--){
        if (n%2==0){
            answer+= n;
        }
    }
    return answer;
}