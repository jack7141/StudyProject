
def dfs(x,y):
    if x <= -1 or x >= n or y <=-1 or y >=m:
        return False
        # 현재 노드 아직 방문 안했으면?
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상하좌우 재귀호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True

    return False



n, m = map(int, input().split())
# 2차원 리스트
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

print(graph)
# 모든 노드에 대해서 값 채우기
result = 0
for i in range(n):
    for j in range(m):
        # dfs 수행
        if dfs(i, j) == True:
            result += 1

print(result)


