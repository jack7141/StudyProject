from collections import deque
import queue

def bfs(x, y):
    # 큐 
    queue = deque()
    queue.append((x, y))

    while queue:
        # FIFO
        x, y = queue.popleft()

        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            '''
            dx = [-1, 1, 0, 0]
            nx = x + dx[i]
            0: -1, 1, 0, 0
            1: 0, 2, 1, 1
            2: 1, 3, 2, 2
            3: 2, 4, 3, 3
            '''
            nx = x + dx[i]
            '''
            dy = [0, 0, -1, 1]
            ny = y + dy[i]
            0: 0, 0, -1, 1
            1: 1, 1, 0, 2
            2: 2, 2, 1, 3
            3: 3, 3, 3, 4
            '''
            ny = y + dy[i]

            # 미로에서 공간 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]


n, m = 4, 5
# 2차원 리스트
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 방향 4가지 정의(상, 하, 좌, 우)
'''
(1,1) (1,2) (1,3)
(2,1) (2,2) (2,3)
(3,1) (3,2) (3,3)
'''
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))

# ==================================================================================================================
# 내스타일 DFS
from collections import deque
import sys
sys.setrecursionlimit(1000000)
N, M = map(int,input().split())

# N x M 방문 유무 확인 행렬 생성
visited = [[False] * M for _ in range(N)]

# N줄 만큼 입력
graph = [list(map(int, input().strip())) for _ in range(N)]
# 상, 하, 좌, 우
# dx = [0,0,-1,1]
# dy = [1,-1,0,0]
count = 1
def dfs(x, y):
  global count 
  if 0<=x<N and 0<=y<M:    
    if visited[x][y] == False and graph[x][y] == 1:
      visited[x][y] = True
      count += 1
      dfs(x+graph[x][y], y)
      dfs(x-graph[x][y], y)
      dfs(x, y+graph[x][y])
      dfs(x, y-graph[x][y])
      if x == N - 1 and y == M-1:
        print(count)
        return
        
      
  
  # while queue:
  #   x, y = queue.popleft()
  #   for i in range(4):
  #     nx = x + dx[i]
  #     ny = y + dy[i]
  #     if x == N -1 and y == M-1:
  #       print(graph[N -1][M-1])
  #       break
  #     dfs(nx,y)
  #     dfs(x,ny)
      
  # return graph[N-1][M-1]
        
# 모든 행을 이동하면서 탐색할 필요가 없다 왜 why? 연결성을 확인할 필요 없이
# 이동할 수 있는 경우만 파악하면 된다. 
dfs(0,0)
# # 열
# for x in range(N):
#   # 행
#   for y in range(M):
#     if graph[x][y] == 1 and visited[x][y] == False: 
#       visited[x][y] = True
#       bfs(x,y)

      
    
    
# ==================================================================================================================
# 내스타일 BFS
from collections import deque
N, M = map(int,input().split())

# N x M 방문 유무 확인 행렬 생성
visited = [[False] * M for _ in range(N)]

# N줄 만큼 입력
graph = [list(map(int, input().strip())) for _ in range(N)]
# 상, 하, 좌, 우
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x, y):
  queue = deque()
  queue.append([x, y])  
  
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
        # 끔점이 나오면 끝내주고, 마지막에 누적된 합을 print
      if x == N -1 and y == M-1:
        print(graph[N -1][M-1])
        break
        
      if 0<=nx<N and 0<=ny<M:      
        if visited[nx][ny] == False and graph[nx][ny] == 1:
          graph[nx][ny] = graph[x][y] + 1
          # print(graph[nx][ny])
          visited[nx][ny] = True
          queue.append([nx, ny])
          
  # return graph[N-1][M-1]
        
bfs(0,0)

      
    
    
