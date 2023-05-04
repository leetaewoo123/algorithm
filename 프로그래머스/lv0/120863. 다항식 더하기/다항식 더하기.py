def solution(polynomial):
    answer = ''
    p = polynomial.split(" + ")
    x,n = [],[]
    xn = 0
    for i in p:
        if "x" in i:
            x.append(i[:-1])
        if "x" not in i:
            n.append(int(i))
    nn = sum(n)
    for i in x:
        if i == "":
            xn += 1
        else:
            xn += int(i)
    if len(polynomial)== 1:
        return polynomial
    else:
        if xn > 2 and nn>=1:
            return str(xn)+"x"+" + "+str(nn)
        elif xn > 2 and nn==0:
            return str(xn)+"x"
        elif xn == 0 and nn>=1:
            return str(nn)
        else:
            return "x"+" + "+str(nn)
    
    return xn