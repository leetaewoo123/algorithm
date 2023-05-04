def solution(numbers, target):
    a = [0]
    for i in numbers:
        a = [j+i for j in a] + [j-i for j in a]
        
    return a.count(target)