def solution(s, skip, index):
    ## 97~122
    answer = ''
    
    for i in s:
        j = index
        while j >0:
            i = chr(ord(i)+1)
            if ord(i)>122:
                i = chr(ord(i)%122+96)
            if i in skip:
                continue
            else: j -=1
        
        answer += i
    

    return answer