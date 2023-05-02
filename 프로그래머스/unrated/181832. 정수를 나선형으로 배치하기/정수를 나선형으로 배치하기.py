def solution(n):
    z = [[0]*n for _ in range (n)]
    k,x,y = 1,0,0
    qkdgid = 'right'
    while k <= n*n:
        z[x][y] = k
        k += 1
        
        if qkdgid == 'right':
            if y+1 == n or z[x][y+1] != 0:
                qkdgid = "down"
                x += 1
            else :
                y += 1
        elif qkdgid == "down":
            if x+1 == n or z[x+1][y] != 0:
                qkdgid = "left"
                y -= 1
            else :
                x += 1
        elif qkdgid == "left":
            if y-1<0 or z[x][y-1] != 0 :
                qkdgid = "up"
                x -= 1
            else :
                y -= 1
        elif qkdgid == "up":
            if x-1<0 or z[x-1][y] != 0:
                qkdgid = "right"
                y += 1
            else :
                x -= 1
    return z