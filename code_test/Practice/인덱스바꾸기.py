"""
정수 배열 numbers가 매개변수로 주어집니다.
numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

링크 - https://school.programmers.co.kr/learn/courses/30/lessons/120862
"""

# Sol 1)
def solution(my_string, num1, num2):
    answer = list(my_string)
    answer[num1], answer[num2] = my_string[num2], my_string[num1]
    return "".join(answer)

if __name__ == "__main__":
    print(solution("hello", 1, 2))