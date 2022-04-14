from collections import deque


"""
테스트
1 1 2 2 2 => [1,2 1,2 0]
1 1 2 2 => 1,2 1,2
1 1 2 2 4 => 1 2 4 1 2
1 1 2 2 2 => 1 2 1 2 0

"""
# 2 3 1 5 4
# 2 1 1 2 
# 1 1 2 3 3
# 1 2 0 0 0

n = int(input())
stuffs = list(map(int, input().split()))
stuffs.sort()
dp = [0]*(n+1)
dp[0] = stuffs[0]
stuff_traget = 0

def remove_stuff(dp, stuffs):
  for i in dp:
    if i in stuffs:
      stuffs.remove(i)
  return stuffs

def recursive(stuffs, dp):
  global stuff_traget
  
  if stuff_traget == 0:
    for i in range(len(stuffs)):
      if dp[stuff_traget] < stuffs[i]:
        stuff_traget += 1
        dp[stuff_traget] = stuffs[i]
  else:
    
    for i in range(len(stuffs)):
      if dp[stuff_traget] < stuffs[i]:
        stuff_traget += 1
        dp[stuff_traget] = stuffs[i]
      else:
        dp[stuff_traget] > stuffs[i]
        stuff_traget += 1
        dp[stuff_traget] = stuffs[i]
        
  stuffs = remove_stuff(dp, stuffs)
  if len(stuffs) == 0:
    return
  recursive(stuffs, dp)  
  

recursive(stuffs,dp)

    
print(dp)
print(stuffs)

temp = 0
maximum = 0
for i in range(1, n):
  if dp[i-1] < dp[i]:
    maximum += 1

print(maximum)

