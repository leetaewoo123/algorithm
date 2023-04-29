def solution(a, b, c):
    answer = 0
    n = list(set([a,b,c]))
    if len(n)==1:
        return (3*a)*(3*(a**2))*(3*(a**3))
    elif len(n)==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return sum(n)