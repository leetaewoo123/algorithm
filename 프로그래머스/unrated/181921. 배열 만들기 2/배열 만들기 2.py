def solution(l, r):
    answer = []
    x,y = 1,"0"
    while r > int(y)*5:
        z = x
        y = ""
        while z > 0:
            y += str(z%2)
            z = z//2
        y = y[::-1]
        if int(y)*5>=l and int(y)*5<=r:
            answer.append(int(y)*5)
        x += 1
        
    if len(answer)==0:
        return [-1]    
    return sorted(answer)