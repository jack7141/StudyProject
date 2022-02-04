from itertools import combinations

nums = [3,1,2,3]	
pokemon = len(nums)//2
print(pokemon)
result = list(combinations(nums, pokemon))
# # 결과: [('A', 'B'), ('A', 'C'), ('B', 'C')]
print(set(result))

def solution(nums):
    answer = 0

    print(set(nums))

    leng = len(set(nums))
    
    if len(nums) // 2 > leng:
        return leng
    else:
        return len(nums) // 2

solution(nums=nums)