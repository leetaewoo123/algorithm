def solution(myString):
    a = sorted(myString.split("x"))
    return [n for n in a if n]
    