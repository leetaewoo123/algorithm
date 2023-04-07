def solution(x):
    x_sum = sum(list(map(int,str(x))))
    if x%x_sum==0:
        answer = True
    else : answer =False
    return answer