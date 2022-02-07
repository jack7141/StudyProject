'''
두개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘
'''

import math

a = 192
b = 162

# 최대 공약수(GCD) 계산
print(math.gcd(a,b))


# 최대공약수 재귀형
def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)