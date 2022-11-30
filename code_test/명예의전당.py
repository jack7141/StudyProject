"""
* 프로그래머스
명예의 전당
- https://school.programmers.co.kr/learn/courses/30/lessons/138477?language=python3
"""
import logging

k = 3
score = [10, 100, 20, 150, 1, 100, 200]

def solution(k, score):
    answer = []
    set = []
    for i in score:
        set.append(i)
        a = sorted(set, reverse=True)
        if len(a) <= k:
            answer.append(a[-1])
        else:
            answer.append(a[k-1])
    return answer
if __name__ == "__main__":
    # Loggin 포멧 설정
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    print(solution(k, score))
