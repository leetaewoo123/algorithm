def solution(s):
    s = s.split(" ")
    n = []
    for i in s:
        if i=="Z" and len(n)>= 1:
            n.append(n[-1]*-1)
        else :
            n.append(int(i))
    return sum(n)