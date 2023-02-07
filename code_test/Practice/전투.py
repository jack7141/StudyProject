"""
https://www.acmicpc.net/problem/1303

bfs에서 인자를 바꾸는 이유
https://good-potato.tistory.com/84
https://printscanf.tistory.com/entry/DFS-DFS%EC%97%90%EC%84%9C-xy-%EC%A2%8C%ED%91%9C%EB%A5%BC-%EB%92%A4%EC%A7%91%EB%8A%94%EB%B0%94%EA%BE%B8%EB%8A%94-%EC%9D%B4%EC%9C%A0
"""
import sys
from collections import deque


input = sys.stdin.readline

def bfs(x, y, n, m, graph):
    queue = deque([[x, y]])
    # 상 하
    dx = [-1, 1, 0, 0]
    # 좌 우
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = x + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append([nx, ny])

                # 해당 구역을 살펴보았으므로, 0, 1과 겹치지 않는 값으로 수정 => True, False 같은 플래그 너낌
                queue[nx][ny] = 2
    return 1

if __name__ == "__main__":

    # 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
    for _ in range(int(input())):
        pass
