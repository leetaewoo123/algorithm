def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range (len(completion)):
        if participant[i]!=completion[i]:
            return participant[i]
    
    return participant[len(participant)-1]

# 첫 코드 : 출력은 맞았지만, 효율이 떨어짐
#def solution(participant, completion):
#    
#    for i in completion:
#        if i in participant:
#            participant.remove(i)
#            
#    return participant[0]

