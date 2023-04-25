def solution(board, moves):
    answer = 0
    result = []
    for i in moves:
        for j in range (len(board)):
            if board[j][i-1] != 0:
                result.append(board[j][i-1])
                board[j][i-1] = 0
                break
    answer = samnum(result,answer)
    return answer

def samnum(result,sa):
    for i in range (1,len(result)):
        if result[i]==result[i-1]:
            del result[i-1:i+1]
            sa += 2
            return samnum(result,sa)
    return sa



[[0,0,0,0,0],[0,0,1,0,0],[0,2,5,0,0],[0,2,4,4,2],[0,5,1,3,1]]
[1,5,3,5,1,2,1,4]
4,3,1,1,3,2,