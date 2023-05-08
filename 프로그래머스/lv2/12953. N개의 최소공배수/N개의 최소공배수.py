def solution(arr):
    answer = 1
    for i in arr:
        answer *= i

    for i in range (max(arr),answer+1):
        n = 0
        for j in arr:
            if i%j==0:
                n+=1
            else:
                break
        if n==len(arr):
            return i
                
    
        
    return answer