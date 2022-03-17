n = int(input())

# N x N 방문 유무 확인 행렬 생성
visited = [[False]*n for _ in range(n)]

# N줄 만큼 입력
graph = [list(map(int, input().strip())) for _ in range(n)]

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

count = 0
result = []

def dfs(x, y):
  global count
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 메트릭스 범위 안에서만 처리
    if 0<=nx<n and 0<=ny<n:
      # 범위 안에 있는데, 방문을 안했고, 값이 1이다면 단지로 판단!
      if visited[nx][ny] == False and graph[nx][ny] == 1:
        # 조건식이 통과되면 집으로 판단하고, count UP!!
        count += 1
        visited[nx][ny] = True
        # 해당 번호부터 재귀로 상,하,좌,우 탐색
        dfs(nx, ny)
        


# x
for x in range(n):
  # y
  for y in range(n):
    if graph[x][y] == 1 and visited[x][y] == False:
      visited[x][y] == True
      count = 0
      dfs(x, y)
      result.append(count)


print(len(result))
result.sort()
for i in result:
  print(i)

# 위의 방법이 잘 안되서 아래 방법으로 다시 품
# ========================      
N = int(input())

# N x N 방문 유무 확인 행렬 생성
visited = [[False] * N for _ in range(N)]
# N줄 만큼 입력
graph = [list(map(int, input().strip())) for _ in range(N)]
# 상, 하, 좌, 우
dx = [0,0,-1,1]
dy = [1,-1,0,0]

each = 0
result = []

def dfs(x, y):
    global each
    # 범위 벗어나면 중단
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
      
    # 범위 안에 있는데, 방문을 안했고, 값이 1이다면 단지로 판단!
    if visited[x][y] == False and graph[x][y] == 1:
      # 조건식이 통과되면 집으로 판단하고, count UP!!
      each += 1
      # 방문으로 표시
      visited[x][y] = True
      
      # 해당 번호부터 재귀로 상,하,좌,우 탐색
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx, ny)
        
      return True
    return False

# x
for x in range(N):
  # y
  for y in range(N):
    if dfs(x, y) == True:
      result.append(each)
      each = 0

print(len(result))
result.sort()
for i in result:
  print(i)

      
    
    

    
    
