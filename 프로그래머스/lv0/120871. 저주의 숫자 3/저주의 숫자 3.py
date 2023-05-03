def solution(n):
    answer,k = 0,0
    a = []
    
    while k < n:
        if (answer%3 != 0) and ("3" not in str(answer)):
            k+= 1
            a.append(answer)
            answer += 1
        else :
            answer +=1
    return a[-1]