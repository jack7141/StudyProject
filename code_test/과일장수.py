from itertools import permutations

"""
리스트에서 각각의 점수를 통해서 등수를 구하는 방법
"""



def solution(grade):
    answer = []
    for i in range(0, len(grade)):
        r = 1
        for j in range(0, len(grade)):
            if grade[i] < grade[j]:
                r += 1
        answer.append(r)
    return answer

grade = [2,2,1]
# grade = [3,2,1,2]


if __name__ == "__main__":
    # print(solution(a, b, budget))
    print(solution(grade))