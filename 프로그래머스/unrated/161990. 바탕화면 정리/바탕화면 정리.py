def solution(wallpaper):
    answer = []
    dot_min_x,dot_min_y,dot_max_x,dot_max_y = [],[],[],[]
    
    for i in range (len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j]=="#":
                dot_min_x.append(i)
                dot_min_y.append(j)
                dot_max_x.append(i+1)
                dot_max_y.append(j+1)
    
    if len(dot_min_x)==1:
        answer= dot_min_x+dot_min_y+dot_max_x+dot_max_y
    else :
        answer = [min(dot_min_x)]+[min(dot_min_y)]+[max(dot_max_x)]+[max(dot_max_y)]
    return answer