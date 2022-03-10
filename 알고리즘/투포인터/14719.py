# 투포인터 방식으로 양쪽끝을 기준으로 서로 비교해가면서 푸는 방식으로 접근
# 백준 14719 빗물문제
# ex) 4 4
h, w = map(int, input().split())

# ex) 3 0 1 4
block_height = list(map(int, input().split()))

left_point, right_point = 0, w-1

# 가장 첫번쨰 점을 기준으로 시작[맨 왼쪽]
max_left = block_height[left_point]

# 가장 끝점을 기준으로 시작[맨 오른쪽]
max_right = block_height[right_point]

result = 0

# 왼쪽기준과 오른쪽 기준이 같아질때까지
while left_point < right_point:
  """
  1. max_left = max(3, 3)
  2. max_left = max(3, 0)
  3. max_left = max(3, 1)
  4. break Point
  """
  
  max_left = max(max_left, block_height[left_point])
  """
  1. max_right = max(4, 4)
  """
  max_right = max(max_right, block_height[right_point])

  # 비교!
  if max_left >= max_right:
    result += max_right - block_height[right_point]
    right_point -= 1
    
  if max_left < max_right:
    result += max_left - block_height[left_point]
    left_point += 1
    
  print(result)