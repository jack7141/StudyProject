'''
코드업
동적계획법
n의 k승 구하기 2

[문제] 
어떤 정수 n과 k가 입력되면, nk의 값을 1,000,000,007로 나눈 나머지를 출력하시오.

[입력]
공백을 기준으로 int 범위의 정수 n과 k가 주어진다. (1<=n<=100,000, 1<=k<=100,000,000)

n, k = input().split(' ')
n = int(n)
k = int(k)

[출력]
nk의 결과를 출력한다.

[입출력예시]
4 2 = 16
'''
# FIXME: 1. 메모리 오류
def solution(n: int, k:int):
    # 중복 계산값이면 배열을 이용
    divide = 1000000007
    return n**k % divide

print(solution(n=2, k=5))