def solution(box, n):
    q = 1
    for i in box:
        q *= int(i / n)
    return q