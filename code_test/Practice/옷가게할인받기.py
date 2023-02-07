from itertools import permutations, combinations

"""
리스트에서 각각의 점수를 통해서 등수를 구하는 방법
"""


from collections import Counter
import re


def solution(price):
    # 아무런 조건이 없으면 할인없이 계산
    answer = price
    if price >= 100_000 and price < 300_000:
        answer = price - (price * 0.05)
    elif price >= 300_000 and price < 500_000:
        answer = price - (price * 0.1)
    elif price >= 500_000:
        answer = price - (price * 0.2)
    return int(answer)

if __name__ == "__main__":
    print(solution(580000))

