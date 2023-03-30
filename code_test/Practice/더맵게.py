"""
https://www.acmicpc.net/problem/1303

bfs에서 인자를 바꾸는 이유
https://good-potato.tistory.com/84
https://printscanf.tistory.com/entry/DFS-DFS%EC%97%90%EC%84%9C-xy-%EC%A2%8C%ED%91%9C%EB%A5%BC-%EB%92%A4%EC%A7%91%EB%8A%94%EB%B0%94%EA%BE%B8%EB%8A%94-%EC%9D%B4%EC%9C%A0
"""
import heapq
import sys
from collections import deque
import heapq

def solution(jobs):
    answer = 0
    start, now, heap = -1, 0, []
    while heap or jobs:
        while jobs and start < jobs[0][0] <= now:
            req, time = jobs.pop(0)
            heapq.heappush(heap, (time, req))
        if heap:
            time, req = heapq.heappop(heap)
            start = now
            now += time
            answer += now - req
        else:
            now = jobs[0][0]
    return int(answer // len(jobs))

import random
def rand5():
    """
    rand7() 함수는 1~7의 숫자 중 하나를 반환합니다.
    """

    num = 0
    while num == 0:
        rand7 = random.randrange(1, 8)
        num = (rand7 - 1) * 7 + rand7  # 1부터 49까지의 숫자를 랜덤하게 생성
    return (num % 5) + 1

def rand5():
    while True:
        rand7 = random.randrange(1, 8)
        num = (rand7 - 1) * 7 + rand7
# def rand5():
#     while True:
#         num = (rand7() -1) * 7 + rand7() # 1~49까지 랜덤하게 생성
#
# def rand7():
#     num = 0
#     while num < 1 or num > 7:  # 1부터 7까지의 숫자 중 하나가 나올 때까지 반복
#         num =  (rand5() - 1)  * 5 + rand5()  # 1부터 25까지의 숫자를 랜덤하게 생성
#     return num


if __name__ == "__main__":
    print(rand5())
    # print(solution([[0, 3], [1, 9], [2, 6]]))



