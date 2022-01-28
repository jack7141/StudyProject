'''
문제

어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 단, 두 번째 연산은
N이 K로 나누어떨어질 때만 선택할 수 있다.

1. N에서 1을 뺀다.
2. N을 K로 나눈다.

예를 들어 N이 17, K가 4라고 가정하자. 이때 1번의 과정을 한 번 수행하면 N은 16이 된다. 이후에 2번의 과정을 두 번
수행하면 N은 1이 된다. 결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 된다. 이는 N을 1로 만드는 최소 횟수이다.
N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.

'''

# 아이디어 최대한 K값으로 나누는것을 목표로한다
# 나눠지는지 확인? 나누기 count : N-1 count

from ast import While
from unittest import result


N = 17
K = 4
count = 0
while True:
    # 나눠떨어지는가?
    print('='*13)
    print(f'N: {N}')
    print(f'count: {count}')
    if N%K == 0:
        # N에 몫을 담는다
        N //= K
        count += 1
    else:
        N -= 1
        count += 1

    if N == 1:
        break

print('='*13)
print(count)

'''
* 시간 복잡도 O(log)

result = 0
while True:
    # 17 // 4 = 4 * 4
    # target = 16, 4
    target = (N // K) * K
    print(target)
    # result = 17 - 16 = 1
    # result = 4 - 4 = 0
    result += (N - target)
    print(result)
    # 16
    N = target
    print(N)
    if N < K:
        break
    # result = 2
    result += 1
    
    # N = 4
    N //= K
    print(N)
    print('='*7)

result += (N - 1)
print(result)
'''