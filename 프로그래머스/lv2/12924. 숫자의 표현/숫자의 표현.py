def solution(n):
    answer,cnt = 0,0
    k = 1
    while k<=n:
        answer =0
        for i in range (k,n+1,1):
            answer += i
            if answer > n :
                k += 1
                break
            if answer == n:
                cnt += 1
                k += 1
                break
    return cnt