

# n, m = map(int, input().split())
#
# graph = []
#
# for _ in range(n):
#     graph.append(list(map(int, input())))

graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

n, m = 4, 5
def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 내가 재귀가 약하네
        # 첫 지점에서 상하좌우를 조회했을때 더이상 갈 곳이 없게되면 True로 반환
        # 아니면 계속 False
        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x - 1, y)
        return True
    return False
ice_cream_count = 0
for x in range(n):
    for y in range(m):
        if dfs(x, y):
            ice_cream_count += 1

print(ice_cream_count)

