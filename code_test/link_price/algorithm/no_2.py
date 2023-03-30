"""
* 지정한 범위의 자연수의 집합에서 소수의 개수와 소수를 모두 곱한 값을 구하는 코드를 작성하세요.
Input :
  start = 2
  end = 20

Output Print 샘플:
  count = 5? 8 아닌가?..
  total = 2 * 3 * 5 * 7 * .... =
"""
from functools import reduce

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def solution(start, end):
    prime_list = [i for i in range(start, end + 1) if is_prime(i)]
    print(len(prime_list))
    print('total =', ' * '.join(map(str, prime_list)), '=', reduce(lambda x, y: x * y, prime_list))

if __name__ == "__main__":
    solution(start=2, end=20)