def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    cnt_a,cnt_b,cnt_c = 0,0,0
    for i in range (0,10001):
        a.append(a[i%5])
        b.append(b[i%8])
        c.append(c[i%10])
    
    for i in range (len(answers)):
        if a[i]==answers[i]:
            cnt_a += 1
        if b[i]==answers[i]:
            cnt_b += 1
        if c[i]==answers[i]:
            cnt_c += 1
            
    cnt_all = [cnt_a, cnt_b, cnt_c]
    
    for i in range (3):
        if max(cnt_all) == cnt_all[i]:
            answer.append(i+1)
    
    return answer