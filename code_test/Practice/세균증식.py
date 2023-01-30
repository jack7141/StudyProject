"""
정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다.
배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.

링크 - https://school.programmers.co.kr/learn/courses/30/lessons/120844
"""

# Sol 1)
def solution(numbers, direction):
    answer = numbers
    if direction == "right":
        num = answer.pop()
        answer.insert(0, num)
    else:
        num = answer.pop(0)
        answer.append(num)
    return answer

# Sol 2)
# deque를 사용하여 리스트 회전을 용이하게 처리할 수 있음
from collections import deque
def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == "right":
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)

if __name__ == "__main__":
    print(solution([1, 2, 3], "right"))
    print(solution([4, 455, 6, 4, -1, 45, 6], "left"))