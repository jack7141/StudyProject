from itertools import permutations, combinations

"""
리스트에서 각각의 점수를 통해서 등수를 구하는 방법
"""


from collections import Counter
import re


def solution(array):
    answer = 0
    # counter로 각각의 값들의 갯수 파악
    array_counter = Counter(array)
    # 카운터에서 가장 큰 수는
    order = array_counter.most_common()
    maximum = order[0][1]

    modes = []

    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
    if len(modes) == 1:
        return modes[0]
    else:
        return -1


if __name__ == "__main__":
    print(solution([1, 2, 3, 3, 3, 4]))

