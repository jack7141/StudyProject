"""
정수 배열 numbers가 매개변수로 주어집니다.
numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

링크 - https://school.programmers.co.kr/learn/courses/30/lessons/120862
"""

# Sol 1)
# def solution(numbers):
#     answer = 0
#     if len(numbers) == 2:
#         answer = numbers[0]*numbers[1]
#     for i in range(0, len(numbers)):
#         for j in range(i+1, len(numbers)):
#             max = numbers[i]*numbers[j]
#             if  max > answer:
#                 answer = max
#     return answer

# Sol 2)
# 정렬을 하고 나면, 최대와 최소가 각각의 맨 마지막에 모이게 된다.
# EX) -31, 0, 1, 9, 10, 24
# 이 상태에서 앞의 2개와 뒤의 2개만 비교하면 최대값을 알 수 있음,
# 왜냐하면 앞의 두수가 서로 음수일 경우도 비교가 가능해짐
def solution(numbers):
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2])

if __name__ == "__main__":
    print(solution([0, -31, 24, 10, 1, 9]))