def solution(k, m, score):
    answer = 0
    n=0
    score = sorted(score)
    score.reverse()
    
    for i in range (0,len(score),m):
        if n == int(len(score)/m):
            break
        else : 
            answer += min(score[i:i+m])*m
            n+=1
        
    return answer