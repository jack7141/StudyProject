"""
링크 - https://school.programmers.co.kr/learn/courses/30/lessons/87946
"""
# from collections import deque
# def solution(k, dungeons):
#     answer = -1
#     test = sorted(dungeons, key = lambda x : (x[0], x[1]))
#     test_roate = deque(test)
#     for _ in range(len(dungeons)):
#         test_roate.rotate(1)
#         hp = k
#         for i in test_roate:
#             if i[0] <= hp:
#                 hp -= i[1]
#
#         print(test_roate)
#     return answer
#
#

# 일단 경우의 수!의 문제가 나오면 펄뮤테이션으로 돌리면 될거같은데, 시간초과가 나게될 수도 있지 않나?
from itertools import permutations
def solution(k, dungeons):
    dun_num = len(dungeons)
    answer = 0

    for permut in permutations(dungeons, dun_num):
        hp = k
        count = 0
        for pm in permut:
            if hp >= pm[0]:
                hp -= pm[1]
                count += 1
        if count > answer:
            answer = count

    return answer
if __name__ == "__main__":
    print(solution(80, [[80,20],[50,40],[30,10]]))