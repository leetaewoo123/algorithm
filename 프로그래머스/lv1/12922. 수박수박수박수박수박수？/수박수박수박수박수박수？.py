def solution(n):
    answer = ''
    cnt = 1
    for i in range(n):
        if cnt%2==0:
            answer += "박"
        else : answer += '수'
        cnt+=1
    return answer