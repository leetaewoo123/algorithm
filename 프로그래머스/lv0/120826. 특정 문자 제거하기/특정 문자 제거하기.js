function solution(my_string, letter) {
    answer = '';
    for (i = 0; i<my_string.length; i++){
        if (my_string[i]==letter){
            continue;
        } else {
            answer += my_string[i];
        }
    }
    return answer;
}