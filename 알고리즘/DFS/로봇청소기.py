office = [[5,-1,4],[6,3,-1],[2,-1,1]]
move = ["go","go","right","go","right","go","left","go"]
r = 1
c = 0
m = len(office)
# 이동할 방향 4가지 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 방문 유무 확인
checkpoint = [[False] * m for _ in range(m)]
checkpoint[r][c] = True
for i in checkpoint:
  print(i)


road = []
from collections import deque
def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  print(queue)
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 공간 벗어나면 예외
      if nx < 0 or nx >= m or ny < 0 or ny >= m:
        continue
      if office[nx][ny] == -1:
        continue
      if office[nx][ny] > 0:
        road.append((nx, ny))
  return road



    

print(bfs(r, c))