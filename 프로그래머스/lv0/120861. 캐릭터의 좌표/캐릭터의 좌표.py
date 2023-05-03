def solution(keyinput, board):
    start = [0,0]
    for i in keyinput:
        if i == 'left' and (start[0] > int(-1*board[0]/2)):
            start[0] -= 1
        elif i == 'right' and (start[0] < int(board[0]/2)):
            start[0] += 1
        elif i == 'up' and (start[1] < int(board[1]/2)):
            start[1] += 1
        elif i == 'down' and (start[1] > int(-1*board[1]/2)):
            start[1] -= 1
    return start