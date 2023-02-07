"""
링크 - https://school.programmers.co.kr/learn/courses/30/lessons/87946
"""
from collections import defaultdict, deque
from itertools import permutations
from operator import itemgetter

import functools

# def solution(maps):
#     answer = 0
#     # 처음 시작할 상하좌우를 담아준다.
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#
#     # 처음 시작할 위치를 담아준다.
#     queue = deque([[0, 0]])
#
#     while queue:
#         x, y = queue.popleft()
#         # 상하좌우 칸 확인하기
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             # 맵 벗어나면 무시
#             if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
#                 continue
#
#             # 벽이면 무시
#             if maps[nx][ny] == 0:
#                 continue
#
#             # 처음 지나가는 길이면 거리계산하고 다시 상하좌우 확인하기
#             if maps[nx][ny] == 1:
#                 maps[nx][ny] = maps[x][y] + 1
#                 queue.append([nx, ny])
#
#     # 상대 팀 진영(제일 오른쪽 아래 칸)까지의 거리 반환
#     answer = maps[len(maps) - 1][len(maps[0]) - 1]
#
#     return answer if answer > 1 else -1

def solution(maps):
    answer = 0
    # 상 하
    dx = [-1, 1, 0, 0]
    # 좌 우
    dy = [0, 0, -1, 1]
    queue = deque([[0, 0]])

    # 벽, 길 변수생성
    wall, road = 0, 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            # 동적으로 상하좌우 움직임 생성
            nx = x + dx[i]
            ny = x + dy[i]

            # 맵을 벗어났을 경우 무시
            if nx < 0 or nx >= len(maps) or ny >= len(maps[0]) or ny < 0:
                continue

            # 벽이면 무시
            if maps[nx][ny] == wall:
                continue

            if maps[nx][ny] == road:
                maps[nx][ny] = maps[x][y] + 1
                queue.append([nx, ny])

    # 맵이 끝났을때, 결과 반환
    answer = maps[len(maps) - 1][len(maps[0]) - 1]

    if answer > 1:
        return answer
    else:
        return -1

if __name__ == "__main__":
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
