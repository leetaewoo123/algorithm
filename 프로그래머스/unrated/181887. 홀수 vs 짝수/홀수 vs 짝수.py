def solution(num_list):
    a = [num_list[i] for i in range (0,len(num_list),2)]
    b = [num_list[i] for i in range (1,len(num_list),2)]
    return max(sum(a),sum(b))