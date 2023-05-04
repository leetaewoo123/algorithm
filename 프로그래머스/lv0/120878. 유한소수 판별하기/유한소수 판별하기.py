def solution(a, b):
    answer = 0
    
    for i in range (b,1,-1):
        if a%i == 0 and b%i == 0:
            a=a//i
            b=b//i

    while True:
        if b%2 == 0:
            b=b//2
        elif b%5 == 0:
            b=b//5
        else :
            break
    if b==1:
        return 1
    else:
        return 2