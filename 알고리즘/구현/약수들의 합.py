# 요약
def solution(n):
    return sum([i for i in range(1, n+1) if n % i == 0])


# 클린코드
num = 12
for i in range(1, num+1):
    if num % i == 0:
        # 약수임
        print(i, end=' ')
print()