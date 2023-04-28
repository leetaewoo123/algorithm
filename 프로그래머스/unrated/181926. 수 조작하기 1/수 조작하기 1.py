def solution(n, control):
    num = {"w": 1, "s":-1, "d":10, "a":-10}
    for i in control:
        n += num[i]
    return n