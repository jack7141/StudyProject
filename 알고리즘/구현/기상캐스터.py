from collections import deque
N, M = map(int,input().split())

# N x M 방문 유무 확인 행렬 생성
visited = [[-1] * M for _ in range(N)]
# N줄 만큼 입력
graph = [list(map(str, input())) for _ in range(N)]

def bfs(x, y):
  count = 0
  queue = deque()
  queue.append([x, y])  
  while queue:
    x, y = queue.popleft()
    # 상하좌우로 움직여본다
    nx = x 
    ny = y + 1
    if 0<=nx<N and 0<=ny<M:      
      if visited[x][y] >= 0 and visited[nx][ny] == -1 and graph[nx][ny] == '.' :
        count += 1
        visited[nx][ny] = count
        queue.append([nx, ny])

# 열
for x in range(N):
#   # 행
  for y in range(M):
    if graph[x][y] == 'c':
      visited[x][y] = 0
      bfs(x, y)
# print(graph)
for i in visited:
  print(*i)