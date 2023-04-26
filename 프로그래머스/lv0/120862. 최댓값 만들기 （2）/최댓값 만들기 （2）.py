def solution(numbers):
    answer = 0
    numbers = sorted(numbers)
    if numbers[0] < 0 and numbers[1] < 0:
        return max(numbers[0]*numbers[1],numbers[-1]*numbers[-2])
    else :
        return numbers[-1]*numbers[-2]