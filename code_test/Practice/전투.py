"""
https://www.acmicpc.net/problem/1303

bfs에서 인자를 바꾸는 이유
https://good-potato.tistory.com/84
https://printscanf.tistory.com/entry/DFS-DFS%EC%97%90%EC%84%9C-xy-%EC%A2%8C%ED%91%9C%EB%A5%BC-%EB%92%A4%EC%A7%91%EB%8A%94%EB%B0%94%EA%BE%B8%EB%8A%94-%EC%9D%B4%EC%9C%A0
"""
import sys
from collections import deque


input = sys.stdin.readline
#
# def bfs(x, y, n, m, graph):
#     queue = deque([[x, y]])
#     # 상 하
#     dx = [-1, 1, 0, 0]
#     # 좌 우
#     dy = [0, 0, -1, 1]
#     while queue:
#         x, y = queue.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = x + dy[i]
#
#             if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
#                 queue.append([nx, ny])
#
#                 # 해당 구역을 살펴보았으므로, 0, 1과 겹치지 않는 값으로 수정 => True, False 같은 플래그 너낌
#                 queue[nx][ny] = 2
#     return 1
#
#
# def solution(n, m, x_axis, y_axis):
#     x_big = 0
#     if len(x_axis) == 0:
#         # 좌표가 없을 경우
#         x_big = n
#     # 좌표가 한개인 경우
#     elif len(x_axis) == 1:
#         x_big = x_axis[0]
#         # x 좌표 하나를 기준으로 어느것이 더 큰가? 비교
#         if n - x_axis[0] <= x_big:
#             x_big = x_big
#         else:
#             x_big = n - x_axis[0]
#     else:
#         # 좌표가 여러개인 경우 전체 탐색
#         for index_x in range(len(x_axis)):
#             if index_x == 0:
#                 x_big = x_axis[index_x]
#             # 주어진 좌표가 끝까지 갔을 경우는
#             elif index_x == len(x_axis) - 1:
#                 if x_axis[index_x] - x_axis[index_x - 1] <= x_big:
#                      x_big = x_big
#                 else:
#                     x_big = x_axis[index_x] - x_axis[index_x - 1]
#                 if n - x_axis[index_x] <= x_big:
#                     x_big = x_big
#                 else:
#                     x_big = n - x_axis[index_x]
#             else:
#                 if x_axis[index_x] - x_axis[index_x - 1] <= x_big:
#                      x_big = x_big
#                 else:
#                     x_big = x_axis[index_x] - x_axis[index_x - 1]
#
#     return 0

from collections import Counter
from itertools import combinations

from collections import defaultdict


def solution(A):
    n = len(A)
    letters = defaultdict(int)
    for string in A:
        for letter in string:
            letters[letter] += 1

    max_length = 0
    for string in A:
        length = len(string)
        for i in range(length):
            if letters[string[i]] == 1:
                max_length = max(max_length, length)
                break
            else:
                letters[string[i]] -= 1
                length -= 1
        for letter in string:
            letters[letter] += 1
    return max_length


if __name__ == "__main__":
    # print(solution(4, 4, [1], [3]))  # 5

    print(solution(['co', 'dil', 'ity']))
    # print(solution([12, 12, 12, 15, 10]))
    # print(solution([18, 26, 18, 24, 24, 20, 22]))
    # # 가로 크기 N, 세로 크기 M이 주어진다.
    # m, n = map(int, input().split())
    # graph = [list(input().strip()) for _ in range(n)]
    # w, b = 0, 0
    # # 가로
    # for i in range(n):
    #     # 세로
    #     for j in range(m):
    #         if graph[i][j] != 0:
    #             if graph[i][j] == 'W':
    #                 # 뭉쳐있으면 위력이 제곱이 된다.
    #                 w += bfs(i, j, graph[i][j]) ** 2
    #             else:
    #                 b += bfs(i, j, graph[i][j]) ** 2
