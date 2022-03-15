import sys

n = int(input())
numbers = []
for _ in range(n):
     numbers.append(int(sys.stdin.readline()))  
sorted_number = sorted(numbers,reverse=True)
start_pos = 0
end_pos = len(numbers)
divide = 3
result = 0
for index in range(start_pos,end_pos,divide):
  # print(sorted_number[start_pos:start_pos+divide])
  product = sorted_number[start_pos:start_pos+divide]
  start_pos = start_pos + divide
  if len(product) == 3:
    result+=sum(product[:2])
  else:
    result+=sum(product)
print(result)

# 다른 풀이
from sys import stdin
n=int(input())
m=list(map(int, stdin.read().split()))
# 내림차순으로 정렬
m.sort(reverse=True)
cost = 0

for i in range(n):
	# 내림차순으로 정렬을 해놨으니, 3번째로 들어오게 되는 값만 제외시키면 정답이 된다.
    # ex) cost += m[0],m[1],m[3],m[4],m[6],m[7]...
    # 훨씬 간결한거같다...
    if(i%3!=2):
        cost += m[i]
print(cost)