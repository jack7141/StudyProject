'''
코드업
동적계획법
피보나치 수열

[문제] 
피보나치 수열이란 앞의 두 수를 더하여 나오는 수열이다.

첫 번째 수와 두 번째 수는 모두 1이고, 세 번째 수부터는 이전의 두 수를 더하여 나타낸다. 피보나치 수열을 나열해 보면 다음과 같다.

1, 1, 2, 3, 5, 8, 13 …

자연수 N을 입력받아 N번째 피보나치 수를 출력하는 프로그램을 작성하시오.

[입력]
자연수 N이 입력된다. (N은 40보다 같거나 작다.)

[출력]
N번째 피보나치 수를 출력한다.
'''

def Fibonacci_Memoization(number: int):
    fibo = [0,1] 

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
print(Fibonacci_Memoization(7))

