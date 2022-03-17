from collections import deque
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 방문 유무 확인
visited = [[False]*3 for _ in range(N)]

# 오른쪽만 가능
dx = [1,0]

# 아래만 가능
dy = [0,1]

def dfs(x, y):
  
  q = deque()
  q.append([x,y])
  
  # 주어진 범위를 벗어나는 경우 즉시 종료
  # x, y의 범위가 0,0보다 작아지거나, 주어진 matrix의 크기를 초과하는 경우
  while q:
    x, y = q.popleft()
    step = graph[x][y]

    # 끝점이 -1이므로 -1로 도달하면 성공!
    if graph[x][y] == -1:
      return True
    for move in range(2):
      nx = x+dx[move]*step
      ny = y+dy[move]*step
      # 범위 벗어나면 무시
      if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue

      # 방문하지 않았을경우만
      if not visited[nx][ny]:
        visited[nx][ny] = True
        q.append([nx, ny])  
        
if dfs(0,0):
    print('HaruHaru')
else:
    print('Hing')

# +=========================================================================
# dfs를 이용한 풀이
import sys
input=sys.stdin.readline


def dfs(x,y) :
    #영역을 벗어났거나 이미 방문을 했다면 return
    if x<=-1 or x>=N or y<=-1 or y>=N or visit[x][y]==1:
        return
    
    #방문한 곳의 이동 칸 수가 -1이라면 방문처리를 해주고 return 한다. 
    if graph[x][y] == -1 :
        visit[x][y] = 1
        return

    #방문했다고 표시해준다.
    visit[x][y]=1

    #상,하,좌,우를 요소 수만큼 점프하여 방문한다.
    dfs(x+graph[x][y],y)
    dfs(x-graph[x][y],y)
    dfs(x,y+graph[x][y])
    dfs(x,y-graph[x][y])



#게임 구역의 크기 N을 입력받는다.
N=int(input())

#게임판의 구역을 입력받는다. 2차원 리스트
graph=[list(map(int,input().split())) for _ in range(N)]

#방문여부를 저장할 visit 2차원 리스트를 만든다.
visit=[[0]*N for _ in range(N)]

#출발은 0,0에서 하므로 dfs(0,0)을 호출한다.
dfs(0,0)

#결과 출력
if visit[-1][-1] == 1 :
    print('HaruHaru')
else :
    print('Hing')
