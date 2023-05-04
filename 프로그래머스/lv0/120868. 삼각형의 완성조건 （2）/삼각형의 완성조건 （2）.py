def solution(sides):
    answer = 0
    for i in range (1,max(sides)+1):
        if i+min(sides)>max(sides):
            answer += 1
    for i in range (max(sides)+1,sum(sides)):
        answer += 1
    return answer