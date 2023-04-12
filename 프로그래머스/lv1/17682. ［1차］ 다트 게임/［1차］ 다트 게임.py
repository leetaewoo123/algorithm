def solution(dR):
    answer = 0
    n = []
    a = -1
    dR = dR.replace('10','k')
    for i in range (len(dR)):
        if dR[i].isnumeric():
            a += 1
            n.append(int(dR[i]))
        elif dR[i]=='k':
            a += 1
            n.append(10)
        elif dR[i]=="S":
            n[a]== n[a]**1
        elif dR[i]=="D":
            n[a] = n[a]**2
        
        elif dR[i]=="T":
            n[a] = n[a]**3
            
        elif dR[i]=="#":
            n[a] *= -1
            
        elif dR[i]=="*":
            if a>0 :
                n[-1] *= 2
                n[-2] *= 2
            else :
                n[-1] *= 2
        
    return sum(n)