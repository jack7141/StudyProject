"""
이진탐색으로 처리! 
* 리스트의 길이가 길어진다면 이진탐색을 통해서 하는게 효율적이다.
*******여기서는 bisect를 사용해서 풀었다는것이 포인트다!!*******
"""
from bisect import bisect_left, bisect_right
# 상근이가 가지고 있는 카드수
N = int(input())
# [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
N_list = list(map(int,input().split()))

# 정렬
# [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]
N_list.sort()

# 주어지는 정수 갯수
M = int(input())

# [10, 9, -5, 2, 3, 4, 5, -10]
M_list = list(map(int,input().split()))

def bisect_func(N_list, left_value, right_value):
    """  
    parameter
            array : 상근이가 가지고 있는 카드
            left_value : 찾고자하는 값
            right_value : 찾고자하는 값
    """
    # bisect_right : 이진탐색 탐색 모듈로서,
    # 내가 찾고자하는 값의 index + 1값을 반환한다.
    right_index = bisect_right(N_list, right_value)

    # 내가 찾고자하는 값의 index 값을 반환한다.
    left_index = bisect_left(N_list, left_value)

    # 결국 내가 찾고자하는 값의 index부터 index+1까지 찾게 되므로
    # 두 수를 빼면 갯수가 나오게된다
    # EX) 
    # [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
    # [10, 9, -5, 2, 3, 4, 5, -10]
    # left_index: 3
    # right_index : 6(10이 연속되므로 가장 마지막 index + 1을 반환한다.)
    return right_index - left_index

for i in range(M):
    print(bisect_func(N_list, M_list[i], M_list[i]), end=' ')