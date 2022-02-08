'''
알고스팟 운영진이 모두 미로에 갇혔다. 미로는 N*M 크기이며, 
총 1*1크기의 방으로 이루어져 있다. 
미로는 빈 방 또는 벽으로 이루어져 있고, 
빈 방은 자유롭게 다닐 수 있지만, 벽은 부수지 않으면 이동할 수 없다.

알고스팟 운영진은 여러명이지만, 
항상 모두 같은 방에 있어야 한다. 즉, 
여러 명이 다른 방에 있을 수는 없다. 
어떤 방에서 이동할 수 있는 방은 상하좌우로 인접한 빈 방이다. 
즉, 현재 운영진이 (x, y)에 있을 때, 이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다. 단, 미로의 밖으로 이동 할 수는 없다.

벽은 평소에는 이동할 수 없지만, 
알고스팟의 무기 AOJ를 이용해 벽을 부수어 버릴 수 있다. 
벽을 부수면, 빈 방과 동일한 방으로 변한다.

만약 이 문제가 알고스팟에 있다면, 
운영진들은 궁극의 무기 sudo를 이용해 벽을 한 번에 다 없애버릴 수 있지만, 안타깝게도 이 문제는 Baekjoon Online Judge에 수록되어 있기 때문에, sudo를 사용할 수 없다.

현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성하시오.

3 3
0 1 1
1 1 1
1 1 0

# 아이디어
NxM 매드릭스 생성
(1,1)에서 상하좌우 검사 후 0 빈방이 있으면 빈방으로 이동, 없으면 count += 1 => M이랑 동일한 칸까지
1. M의 방향으로 내려갈 수 있으면 먼저 체크

(1, 1)과 (N, M)은 항상 뚫려있다.
'''
from collections import deque

# 이동할 방향 4가지 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# N, M 입력
n, m = map(int, input().split())

# 매트릭스 생성
map = [ list(map(int, input())) for _ in range(m)]

# 방문 유무 확인
checkpoint = [[False] * n for _ in range(m)]
# 맨 처음 값은 무조건 빈방이라고 문제에 조건이 있음.
checkpoint[0][0] = True

def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for k in range(4):
#             # 이동 위치 선정
#             '''
#             nx = x + dx[k]
#             0: -1, 1, 0, 0
#             1: 0, 2, 1, 1
#             2: 1, 3, 2, 2
#             3: 2, 4, 3, 3
#             '''
            nx = x + dx[k]
#             '''
#             ny = y + dy[i]
#             0: 0, 0, -1, 1
#             1: 1, 1, 0, 2
#             2: 2, 2, 1, 3
#             3: 3, 3, 3, 4
#             '''
            ny = y + dy[k]

            # 매트릭스 범위 안인지 Check 공간 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
        
#             # 현 위치에서 내가 갈 수 있는 방향 print
#             print(f'{(x, y)} -> {(nx, ny)}')

            if checkpoint[nx][ny] == False and map[nx][ny] == 0:
                checkpoint[nx][ny] = True
                queue.appendleft((nx, ny))
            else:
                checkpoint[nx][ny] = True
                queue.append((nx, ny))
#             if map[ny][nx] == 0 and checkpoint[ny][nx] == False:
#                 checkpoint[ny][nx] = True
#                 print(f'{(nx, ny)}')
#                 queue.appendleft((nx, ny))
    # return checkpoint[m - 1][n - 1]

print(bfs(0, 0))


'''
4 2
0 0 0 1
1 0 0 0

3 3
0 0 1 
1 0 0 
0 0 1
'''

# BFS 벽을 최소 몇 개 부수어야 하는가?
# from collections import deque
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# m,n = map(int, input().split())
# arr = [ list(map(int, input())) for _ in range(n)]
# dist = [[-1] * m for _ in range(n)]  # 가중치

# q = deque()
# q.append((0,0))

# dist[0][0] = 0

# while q:

#     x,y = q.popleft()
#     for k in range(4):

#         nx = x + dx[k]
#         ny = y + dy[k]

#         if nx < 0 or nx >= n or ny < 0 or ny >= m:
#             continue

#         if dist[nx][ny] == -1 and arr[nx][ny] == 0:
#             dist[nx][ny] = dist[x][y]
#             q.appendleft((nx, ny))
#         else:
#             dist[nx][ny] = dist[x][y] + 1
#             q.append((nx, ny))
# print(dist[n-1][m-1])