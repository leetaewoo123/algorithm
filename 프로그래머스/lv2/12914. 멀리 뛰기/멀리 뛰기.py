def solution(n):
    answer = 0
    cnt = [0,1,2]
    while answer != n:
        cnt.append(cnt[-1]+cnt[-2])
        answer +=1
    return cnt[answer]%1234567