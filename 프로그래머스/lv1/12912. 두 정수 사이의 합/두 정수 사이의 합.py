def solution(a, b):
    answer = 0
    if a>b :
        x = a
        a = b
        b = x
    for i in range (a,b+1):
        answer += i
    return answer