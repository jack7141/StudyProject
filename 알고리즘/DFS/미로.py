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