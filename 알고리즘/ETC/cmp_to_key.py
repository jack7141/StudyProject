"""
2차원 평면 위의 점 N개가 다음과 같이 (x, y) 좌표의 리스트로 주어진다. 
좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

* cmp_to_key는 내 스타일로 정렬을 수정할 수 있는 툴
"""
import functools
 
def comparator(a,b):
    # n에서 숫자 2개를 추출 후! 내 조건식에 대입해서 비교 후 a를 기준으로 정렬!
    # EX) a+b = 610, b+a = 106
    t1, t2 = a+b, b+a
    # 비교!
    print(f"comparator: {a},{b} -> {t1},{t2} -> {(int(t1) > int(t2)) - (int(t1) < int(t2))}")
    # 비교 후 크다: 1 ex) (5 > 4) - (5 < 4)
    # 비교 후 작다: -1 ex) (3 > 4) - (3 < 4)
    # 같다 : 0 ex) (4 > 4) - (4 < 4)

    # 비교 후 a,b 의 순서는 어떻게 정해지는거지? 
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
 
def solution(numbers):
    n = list(map(str, numbers))
    print(f'input -> {n}')
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    print(f'n -> {n}')
    answer = str(int(''.join(n)))
    return answer
 
if __name__ == "__main__":
    print('-' * 40)
    numbers = [[6, 10, 2], [3, 30, 34, 5, 9], [0,0,0,0,0,0]]
    correct_answer = ["6210", "9534330", "0"]
 
    for t in range(len(numbers)):
        answer = solution(numbers[t])
        print('answer :' + answer, '/ correct_answer :' + correct_answer[t])
        if correct_answer[t] == answer:
            print(f'테스트 {t}를 통과하였습니다.')
        else:
            print(f'테스트 {t}를 통과하지 못했습니다.')
        print('-'* 40)