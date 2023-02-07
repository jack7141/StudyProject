from itertools import permutations

"""
리스트에서 각각의 점수를 통해서 등수를 구하는 방법
"""

def solution(n, lost, reserve):
    answer = 0

    # 차집합 구하기
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n - len(set_lost)

n, lost, reserve = 5, [2, 4], [1,3,5]

if __name__ == "__main__":
    print(solution(n, lost, reserve))