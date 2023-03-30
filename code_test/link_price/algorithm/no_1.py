"""
* 지정한 범위의 자연수 집합에서 각 숫자의 개수와 각 숫자의 합계를 구하는 코드를 작성하세요

Input :

예제) 10 ~ 15 까지의 각 숫자의 개수를 구하는 경우
10 = 1, 0
11 = 1, 1
12 = 1, 2
13 = 1, 3
14 = 1, 4
15 = 1, 5

Output Print 샘플 :
0 = 1
1 = 7
2 = 1
3 = 1
4 = 1
5 = 1
total = 1 + 0 + 1 + 1 + 1 + 2 + 1 + 3 + 1 + 4 + 1 + 5 = 21
"""
def solution(start, end):
    num = [sum(map(int, j)) for i in range(start, end + 1) for j in str(i)]
    counts = [sum(str(i).count(str(j)) for i in range(start, end + 1)) for j in range(10)]
    for i, count in enumerate(counts):
        if count != 0:
            print(i, '=', count)
    #
    print('total =', ' + '.join(map(str, num)), '=', sum(num))

if __name__ == "__main__":
    solution(start=10, end=15)