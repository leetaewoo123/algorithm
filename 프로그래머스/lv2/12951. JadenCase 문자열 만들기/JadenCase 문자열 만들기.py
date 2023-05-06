def solution(s):
    answer = ''
    word = list(s.lower())
    for i in range(len(word)):
        if word[i].isdigit():
            answer += word[i]
        elif word[i] == ' ':
            answer += word[i]

        elif word[i].isalpha():
            if len(word[0:i]) == 0:
                answer += word[i].upper()
            elif word[i-1] == ' ':
                answer += word[i].upper()
            else:
                answer += word[i]
    return answer