def solution(n):
    n=sorted(list(map(str,str(n))),reverse=True)
    return int("".join(n))