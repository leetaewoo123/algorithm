def solution(citations):
    answer = 0
    c = sorted(citations)
    for i in range (len(c)):
        if c[i] >= len(c)-i:
            answer +=1
            
    return answer