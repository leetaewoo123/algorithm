def solution(a, b, n):
    answer = 0
    while n>=a:
        coke = int(n/a)
        answer += coke*b
        n = n-(coke*a)+coke*b
    return answer