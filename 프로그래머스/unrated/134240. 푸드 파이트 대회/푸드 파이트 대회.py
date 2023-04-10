def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer += int(food[i]/2)*str(i)
    answer_b=list(answer)
    answer_b="".join(reversed(answer_b))
    return str(answer)+"0"+str(answer_b)