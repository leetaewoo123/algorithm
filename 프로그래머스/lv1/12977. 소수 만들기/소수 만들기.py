def solution(nums):
    answer = 0
    
    for i in range (len(nums)):
        for j in range (i+1,len(nums)):
            for z in range (j+1,len(nums)):
                sum_nums = nums[i]+nums[j]+nums[z]
                
                for o in range (2,sum_nums):
                    if sum_nums%o==0:
                        break
                else : answer += 1

    return answer