def solution(array, n):
    z = []
    array = sorted(array)
    for i in array :
        z.append(abs(i-n))
        
    return array[z.index(min(z))]
