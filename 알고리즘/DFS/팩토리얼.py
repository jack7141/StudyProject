'''
n! = 1*2*3*4*...(n-1)*m
'''

# 반복구현
def factorial_iteravice(n):
    result = 1
    for i in range(1, n+1):
        result *= 1
    return result

# 재귀
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

