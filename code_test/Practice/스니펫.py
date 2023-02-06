
# 소수 판별 함수
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True

# 리스트 다중 정렬
# 링크 - https://dailyheumsi.tistory.com/67
# sorted(list, key = lambda x : (x[0], -x[1]))


# deque를 이용한 배열 회전
from collections import deque
def solution(k, test_list):
    # 리스트를 데크로 만들어주고, 로테이트를 치면 회전을 시킬 수 있다.
    # 음수: 왼쪽회전, 양수: 오른쪽회전, 숫자값은 몇칸 돌릴것인지를 결정한다.
    test_roate = deque(test_list)
    for _ in range(len(test_list)):
        test_roate.rotate(1)
        print(test_roate)


def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

import functools
def solution(numbers):
    n = [str(x) for x in numbers]
    # https://velog.io/@heyday_7/python-%EC%A1%B0%EA%B1%B4-%EC%A0%95%EB%A0%AC-%ED%95%98%EA%B8%B0-cmptokey
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer