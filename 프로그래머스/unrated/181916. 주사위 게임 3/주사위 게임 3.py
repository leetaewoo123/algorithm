def solution(a, b, c, d):
    sq = [a,b,c,d]
    sl = list(set(sq))
    if len(sl) ==1:
        return int("".join(map(str,sq)))
    elif len(sl) ==4:
        return min(sq)
    elif len(sl) ==2 :
        if sq.count(sl[0])==sq.count(sl[1]):
            return (sl[0]+sl[1])*abs(sl[0]-sl[1])
        elif sq.count(sl[0])>sq.count(sl[1]):
            return (sl[0]*10+sl[1])**2
        else:
            return (sl[1]*10+sl[0])**2
    else :
        if sq.count(sl[0])>sq.count(sl[1]) and sq.count(sl[0])>sq.count(sl[2]):
            return sl[1]*sl[2]
        elif sq.count(sl[1])>sq.count(sl[0]) and sq.count(sl[1])>sq.count(sl[2]):
            return sl[0]*sl[2]
        else:
            return sl[1]*sl[0]