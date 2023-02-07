"""
* 프로그래머스
명예의 전당
- https://school.programmers.co.kr/learn/courses/30/lessons/138477?language=python3
"""
import logging

number = 10
limit = 3
power = 2
def solution(number, limit, power):
    sum = 0
    for i in range(1, number+1):
        count = 0
        for a in range(1, i+1):
            if i == a:
                count += 1
            elif i % a == 0:
                count += 1
        if count > limit:
            count = power
        sum += count
            # print(i, "의 약수의 개수: ", count)
        print(i, "의 약수의 총 개수: ", count)
    return sum


if __name__ == "__main__":
    # Loggin 포멧 설정
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    print(solution(number, limit, power))
