from itertools import permutations, combinations

"""
리스트에서 각각의 점수를 통해서 등수를 구하는 방법
"""


from collections import Counter
import re


def solution(hp):
    king = hp // 5 # 5로 나눌수 있는 최대 수
    mid = (hp-(king*5)) // 3 # 5로 나눈 수 제외하고 나머지 수 중에서 3으로 나눌수 있는 최대 수
    normal = (hp-(king*5)-(mid*3)) // 1
    return king+mid+normal

if __name__ == "__main__":
    print(solution(23))

