def solution(nums):
    answer = 0
    get = len(nums)/2      # 가질 수 있는 포켓몬 수
    nums = list(set(nums)) # nums의 중복값 제거 후 리스트로 만듬
    if (len(nums) > get) : 
        # 경우의 수가 아니라 선택할 수 있는 포켓몬 종류 개수의 최댓값을 구하는 것이기 때문에 get과 nums를 비교 
        answer = get
    else : answer = len(nums)
    return answer