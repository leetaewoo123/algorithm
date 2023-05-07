def solution(n):
    answer = 0
    k = [0,1]
    for i in range (1,n):
        k.append((k[i-1]+k[i])%1234567)
    return (k[-1]%1234567)
