def solution(n):
    s, k = 1, 2
    while s <= n :
        s *= k
        k += 1
    return k-2