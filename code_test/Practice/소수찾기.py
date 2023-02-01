"""
링크 - https://school.programmers.co.kr/learn/courses/30/lessons/42840
"""
from itertools import combinations, permutations

nums = [1,2,3,4]


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    perm = []
    for i in range(1, len(numbers)+1):
        perm += list(permutations(list(numbers), i))
    nums_list = set(int(''.join(i)) for i in perm)
    for i in nums_list:
        if is_prime(i):
            answer += 1

    return answer

if __name__ == "__main__":
    print(solution("011"))