def solution(n):
    k=0
    for i in range (4,n+1):
        n = 0
        for j in range (2,i):
            if i%j ==0 :
                n += 1
        if n >= 1:
            k += 1
    return k