"""
* 주어진 수 n이 2의 제곱수 인지 판별후, 제곱수가 아니면 0을 반환하고,   2의 제곱수면 2의 몇 제곱인지 반환하세요.

제곱수 인경우
    n = 2
    return 1

제곱수가 아닌경우
    n= 5
    return 0
"""

def solution(n):
    if n <= 0:
        return 0
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    return count if n == 1 else 0

if __name__ == "__main__":
    print(solution(n=5))