from itertools import permutations

"""
리스트에서 각각의 점수를 통해서 등수를 구하는 방법
"""



def solution(k, m, score):
    score = sorted(score, reverse=True)
    answer = 0
    for i in range(0, len(score), m):
        tmp = score[i:i+m]
        if len(tmp) == m:
            answer += min(tmp) * m

    return answer

k = 3
m = 4
score = [1, 2, 3, 1, 2, 3, 1]


if __name__ == "__main__":
    print(solution(k, m, score))