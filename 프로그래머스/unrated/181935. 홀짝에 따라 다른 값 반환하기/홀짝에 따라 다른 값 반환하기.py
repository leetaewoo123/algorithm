def solution(n):
    k = 0
    for i in range (n, 0,-2):
        if n % 2 != 0:
            k += i
        else :
            k += (i**2)
    return k