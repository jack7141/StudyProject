

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


def dfs(x, y):
    if x < 0 or y < 0 or x >=n or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 내가 재귀가 약하네
        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x - 1, y)
        return True
    return False
ice_cream_count = 0
for x in range(n):
    for y in range(m):
        return True
