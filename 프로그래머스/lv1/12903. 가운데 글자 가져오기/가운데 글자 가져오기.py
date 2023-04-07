def solution(s):
    answer = 0
    solve = int(len(s)/2)
    if len(s)%2==1:
        answer = s[solve]
    else : answer =s[solve-1:solve+1]
    return answer