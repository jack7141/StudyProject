"""
https://www.acmicpc.net/problem/1303

bfs에서 인자를 바꾸는 이유
https://good-potato.tistory.com/84
https://printscanf.tistory.com/entry/DFS-DFS%EC%97%90%EC%84%9C-xy-%EC%A2%8C%ED%91%9C%EB%A5%BC-%EB%92%A4%EC%A7%91%EB%8A%94%EB%B0%94%EA%BE%B8%EB%8A%94-%EC%9D%B4%EC%9C%A0
"""
import sys
from collections import deque


def solution(s):
    queue = deque()
    for i in s:
        if i == "(":
            queue.append(i)
        else:
            if queue:
                queue.pop()
            else:
                return False
    if queue:
        return False
    return True

if __name__ == "__main__":
    print(solution(")()("))
