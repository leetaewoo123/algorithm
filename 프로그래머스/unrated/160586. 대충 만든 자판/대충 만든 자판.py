def solution(keymap, targets):
    answer = []
    
    for i in targets:
        w = []
        for j in (list("".join(i))):
            q = []
            for z in keymap:
                if j in z:
                    q.append(z.index(j)+1)
                    
            if len(q) != 0:
                w.append(min(q))
                
        if len(w)==len(i):
            answer.append(sum(w))
        else :
            answer.append(-1)
            
    
    return answer