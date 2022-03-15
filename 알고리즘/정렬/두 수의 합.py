import sys
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

x = int(input())

# 투 포인터 방식으로 첫점과 끝점을 지정해주고, 첫점부터 끝점까지 루프를 돌면서
# 내가 찾는 답이 있는가 없는가를 탐색하는 방식이다.
start_pos = 0
end_pos = len(numbers)-1
count = 0

# 같은 수(같은 리스트의 index)를 더하는일이 없도록,
# 교차하는 경우도 제외하고 작을경우만 while을 돌려준다.
while start_pos < end_pos:
  if numbers[start_pos]+numbers[end_pos] == x:
    start_pos += 1
    count+=1
  elif numbers[start_pos]+numbers[end_pos] < x:
    start_pos += 1
  else:
    end_pos-=1
print(count)