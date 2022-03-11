"""
functools.cmp_to_key(func) 함수는 sorted와 같은 정렬 함수의 key 매개변수에 함수(func)를 전달할 때 사용하는 함수이다. 
단, func 함수는 두 개의 인수를 받아들이고, 
첫번째 인수를 기준으로 그들을 비교하여, 
작으면 음수, 
같으면 0, 
크면 양수(1)를 반환하는 비교 함수이어야 한다.
"""
import functools

def comparator(n1, n2):
    print(n1,n2)
    if n1[1] > n2[1]:         # y 좌표가 크면
        return 1
    elif n1[1] == n2[1]:      # y 좌표가 같으면
        if n1[0] > n2[0]:     # x 좌표가 크면
            return 1
        elif n1[0] == n2[0]:  # x 좌표가 같으면
            return 0
        else:                 # x 좌표가 작으면
            return -1
    else:                     # y 좌표가 작으면
        return -1

def solution(numbers):
    # n = list(map(str, numbers))
    print(f'input -> {numbers}')
    # sorted함수는 0,양수, -1로 판단하기 때문에 0,-1, 양수 값을 리턴해줘야함
    n = sorted(numbers, key=functools.cmp_to_key(comparator),reverse=False)
    print(f'n -> {n}')
    return n


if __name__ == "__main__":
    print('-' * 40)
    # numbers = [(0, 4,1), (1, 2,1), (1, -1,1), (2, 2,1), (3, 3,1)]
    # correct_answer = [(1, -1,1), (1, 2,1), (2, 2,1), (3, 3,1), (0, 4,1)]
    numbers = [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]
    correct_answer = [(1, -1), (1, 2), (2, 2), (3, 3), (0, 4)]
    answer = solution(numbers)
    # for t in range(len(numbers)):
    #     answer = solution(numbers[t])
    #     print('answer :' + answer, '/ correct_answer :' + correct_answer[t])
    #     if correct_answer[t] == answer:
    #         print(f'테스트 {t}를 통과하였습니다.')
    #     else:
    #         print(f'테스트 {t}를 통과하지 못했습니다.')
    #     print('-'* 40)