'''
동적계획법의 핵심인 Memoization을 통해서 간단한 문제를 해결하는 접근법을 배운다.
피보나치 수열을 재귀적인 방식과 Memoization을 통한 방식으로 구현해본다.
문제 피보나치 수열에서 N번째 값을 구하시오!
'''

def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(f'현재 N의 값 : {n}')
        print(f'계산될 N의 값 : {n-1}, {n-2}')
        return Fibonacci(n-1) + Fibonacci(n-2)

# 재귀적 방법
'''
위의 방식으로 하면 피보나치 5의 값을 구하기 위해서 피보나지 4, 3의 값을 알아야하고
피보나치 4의 값을 알기 위해선 3,2의 값을 알아야한다. 즉, 정답을 구하기 위해선 가지치기를
쳐야한다. 논리는 옳지만 효율성이 떨어진다.

'''
# Entry Point
#print(Fibonacci(5))


# 핵심 메모이제이션은 반복되도 결과값은 변화하지 않는 값을 올려놔준다.
def Fibonacci_Memoization(number: int):
    fibo = [0,1] # 처음 수열의 값을 메모리에 올려놓는다.

    for i in range(2, number + 1):
        fibo.append(fibo[i-1] + fibo[i-2])
        '''
        print(fibo)
        [0, 1, 1]
        [0, 1, 1, 2]
        [0, 1, 1, 2, 3]
        [0, 1, 1, 2, 3, 5]
        '''

    return fibo[number]

# Entry Point
print(Fibonacci_Memoization(5))