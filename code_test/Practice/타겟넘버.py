"""
링크 - https://school.programmers.co.kr/learn/courses/30/lessons/87946
"""
from collections import defaultdict, deque
from itertools import permutations
from operator import itemgetter

import functools

# def solution(numbers, target):
#     answer = 0
#     n = len(numbers)
#     # 하위 2가지 방식으로 시작
#     # 1, x, x, x, x
#     # -1, x, x, x, x
#     queue = deque([[numbers[0], 0], [-1*numbers[0], 0]])
#
#     while queue:
#         temp, idx = queue.popleft()
#         idx += 1
#         if idx < n:
#             queue.append([temp + numbers[idx], idx])
#             queue.append([temp - numbers[idx], idx])
#         else:
#             if temp == target:
#                 answer += 1
#     return answer

def solution(numbers, target):
    answer = 0
    # 처음 시작 방법 2가지
    # -1, x, x, x, x
    #  1, x, x, x, x
    queue = deque([[numbers[0], 0], [numbers[0]*-1, 0]])
    n = len(numbers)
    while queue:
        num, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([num + numbers[idx], idx])
            queue.append([num - numbers[idx], idx])
        else:
            if num == target:
                answer += 1
    return answer

if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3))
