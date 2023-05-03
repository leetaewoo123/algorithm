def solution(numlist, n):
    answer = []
    num = []
    for i in numlist:
        num.append(abs(i-n))
        
    while list(set(num))!=[10001]:
        if num.count(min(num)) ==2:
            answer.append(min(num)+n)
            answer.append(min(num)*-1+n)
            num[num.index(min(num))] = 10001
            num[num.index(min(num))] = 10001
        else:
            answer.append(numlist[num.index(min(num))])
            num[num.index(min(num))] = 10001
    return answer