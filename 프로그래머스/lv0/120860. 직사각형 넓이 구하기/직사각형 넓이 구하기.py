def solution(dots):
    answer = 0
    dots = sorted(dots)
    return (dots[1][1]-dots[0][1])*(dots[2][0]-dots[0][0])