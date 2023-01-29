from itertools import permutations

"""
리스트에서 각각의 점수를 통해서 등수를 구하는 방법
"""
from collections import Counter
def solution(s):
    s_dict = Counter(s)
    stack = []
    for i in s:
        if i == '(':  # '('는 stack에 추가
            stack.append(i)
        else:  # i == ')'인 경우
            if stack == []:  # 괄호 짝이 ')'로 시작하면 False 반환
                return False
            else:
                stack.pop()  # '('가 ')'와 짝을 이루면 stack에서 '(' 하나 제거

    return stack == []

s = "[]([[]){}"


if __name__ == "__main__":
    print(solution(s))