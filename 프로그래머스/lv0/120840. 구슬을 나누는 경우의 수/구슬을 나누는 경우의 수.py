def solution(balls, share):
    answer = 0
    bk, sk, ak = 1, 1, 1
    for i in range (1,balls+1):
        bk *= i
    for i in range (1,share+1):
        sk *= i
    for i in range(1,(balls-share)+1):
        ak *= i
        
    return bk/(ak*sk)