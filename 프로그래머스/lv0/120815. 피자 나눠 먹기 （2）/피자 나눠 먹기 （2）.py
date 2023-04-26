def solution(n):
    k,sp = 1,6
    while (sp*k)%n !=0 :
        k += 1
    return k