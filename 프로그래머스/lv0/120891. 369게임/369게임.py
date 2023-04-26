def solution(order):
    k=0
    for i in str(order):
        if int(i) % 3 == 0 and int(i) != 0:
            k += 1 
    return k