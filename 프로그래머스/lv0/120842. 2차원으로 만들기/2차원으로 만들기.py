def solution(num_list, n):
    answer = []
    for i in range (n,len(num_list)+1,n):
        answer.extend([num_list[i-n:i]])
    return answer