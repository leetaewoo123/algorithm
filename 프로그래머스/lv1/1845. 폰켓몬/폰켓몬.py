def solution(nums):
    answer = 0
    get = len(nums)/2
    nums = list(set(nums))
    if (len(nums) > get) :
        answer = get
    else : answer = len(nums)
    return answer