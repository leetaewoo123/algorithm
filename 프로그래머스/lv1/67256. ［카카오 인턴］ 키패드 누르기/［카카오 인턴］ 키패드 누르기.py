def solution(numbers, hand):
    answer = ''
    keypad = [[1,4,7,"*"],[2,5,8,0],[3,6,9,'#']]
    lh,rh = "*","#"
    
    for i in numbers:
        if i in keypad[0]:
            answer += "L"
            lh = i
        elif i in keypad[2]:
            answer += "R"
            rh = i
        else :
            for o in range (3):
                for j in range (4):
                    if keypad[o][j] == i :
                        hl = [o,j]
                    if keypad[o][j] == lh :
                        ll = [o,j]
                    elif keypad[o][j] == rh :
                        rl = [o,j]
            rt = abs(rl[0]-hl[0])+abs(rl[1]-hl[1])
            lt = abs(ll[0]-hl[0])+abs(ll[1]-hl[1])
            
            if rt > lt:
                answer += "L"
                lh = i
            elif rt < lt :
                answer += "R"
                rh = i
            else :
                if hand == "right":
                    answer += "R"
                    rh = i
                else :
                    answer += "L"
                    lh = i
                
    return answer


