from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):
    n1 = numer1*denom2
    d = denom1*denom2
    n2 = numer2*denom1
    n = numer1*denom2+numer2*denom1
    
    for i in range (d,1,-1):
        if n%i == 0 and d%i == 0:
            n = n//i
            d = d//i

    return [n,d]