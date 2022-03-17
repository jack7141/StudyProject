count = 0
def dfs(v):
  global count
  visited[v] = True
  for i in graph[v]:
    # 방문하지 않았다면?
    if not visited[i]:
      dfs(i)
      count+=1

n = int(input())
m = int(input())
visited = [False]*(n+1)

graph = [[]*n for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    # 각 노드들의 간선들 연결
    graph[a].append(b)
    graph[b].append(a)
dfs(1)
print(count)


#=========================================================================
#bfs로 푸는 방식
from collections import deque
n = int(input())
m = int(input())
visited = [False]*(n+1)

def bfs(v):
  
  q = deque()
  q.append(v)
  while q:
    v = q.popleft()
    for i in graph[v]:
      if not visited[i]:
        visited[i] = True
        q.append(i)
      
  
graph = [[]*n for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    # 각 노드들의 간선들 연결
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
print(visited.count(True)-1)