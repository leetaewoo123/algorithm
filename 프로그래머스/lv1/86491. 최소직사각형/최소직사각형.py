def solution(sizes):
    x_max = []
    y_max = []
    for i in range (len(sizes)):
        sizes[i].sort(reverse=True)
    for i in range (len(sizes)):
        x_max.append(sizes[i][0])
        y_max.append(sizes[i][1])
    
    return max(x_max)*max(y_max)