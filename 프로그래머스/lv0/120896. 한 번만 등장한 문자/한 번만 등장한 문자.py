def solution(s):
    answer = ''
    k = list(set(s))
    for i in k:
        if s.count(i)==1:
            answer += i
    return "".join(sorted(answer))