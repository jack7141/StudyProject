"""
https://www.acmicpc.net/problem/1012

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
        """
        * 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)
        * 세로길이 N(1 ≤ N ≤ 50)
        * 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)
        """
        m, n, k = map(int, input().split())

        # 매트리스 생성 [m x n] => 10 x 8
        graph = [[0 for _ in range(m)] for _ in range(n)]



        # 배추 위치값을 매트릭스에 넣어주기
        for i in range(k):
            # 배열은 4사분면이고, 좌표는 1사분면로 이해하면됨
            # 배열에선 [0,0]을 기점으로 내려가면 증가, 오른쪽으로 가면 증가
            # 일반 좌표 평면에선 올라가면 증가, 오른쪽으로 가면 증가
            a, b = map(int, input().split())

            # 그래서 들어오는 값을 아래와 같이 바꿔서 입력해준다.
            graph[b][a] = 1

        count = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 1:
                    count += bfs(i, j, n, m, graph)
        print(count)

