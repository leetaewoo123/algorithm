def solution(k, score):
    answer = []
    num = []
    
    for i in range (len(score)):
        
        if len(num)<k:
            num.append(score[i])
            answer.append(min(num))
            
        elif len(num)==k :
            if score[i]<min(num):
                answer.append(min(num))
            else :
                num.remove(min(num))
                num.append(score[i])
                answer.append(min(num))

    return answer