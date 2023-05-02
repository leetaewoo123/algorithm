def solution(numbers, k):
    answer = 0
    h = int(len(numbers)/2+0.5)
    numbers *= k
    n = 0
    for i in range (0,len(numbers),2):
        n+=1
        if n == k:
            return numbers[i]