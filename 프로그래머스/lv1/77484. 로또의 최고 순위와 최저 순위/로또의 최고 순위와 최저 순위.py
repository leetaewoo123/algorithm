def solution(lottos, win_nums):
    answer = []
    num,zero = 0,0
    lottos.sort()
    win_nums.sort()
    if lottos.count(0)>0:
            zero += lottos.count(0)

    for i in range (len(lottos)):
        if lottos[i] in win_nums:
            num += 1
    if num <=1 and zero ==0:
        answer.extend([6,6])
    elif num<=1:
        answer.extend([7-(zero+num),6])
    else :
        answer.extend([7-(num+zero),7-num])
        
    return answer