def solution(arr):
    n = 0
    while len(arr)>2**n:
        n+=1
    if len(arr)==2**n:
        return arr
    else:
        for i in range (2**n-len(arr)):
            arr.append(0)
    return arr