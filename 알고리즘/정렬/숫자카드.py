"""
이진탐색으로 처리! 
* 리스트의 길이가 길어진다면 이진탐색을 통해서 하는게 효율적이다.
"""

# 상근이가 가지고 있는 카드수
# N = int(input())

#[6, 3, 2, 10, -10]
N_list = list(map(int,input().split()))

# 정렬
# [-10, 2, 3, 6, 10]
N_list.sort()

# 주어지는 정수 갯수
M = int(input())

# [10, 9, -5, 2, 3, 4, 5, -10]
M_list = list(map(int,input().split()))

def binary_search(array, target, start, end):
  """  
  parameter
          array : 상근이가 가지고 있는 카드
          target : 주어진 정수에서 찾고자 하는 카드
          start : 0(리스트 인덱스)
          end : 상근이가 가지고 있는 카드의 길이의 끝점 인덱스   
  """
  # 시작포인트가 end보다 커지면 break
  # 즉 중간 지점을 기준으로 좌, 우로 움직이다 끝점이 start점보다 작아지는 경우 break을
  # 하게된다.
  while start <= end:
    # 두 숫자를 더해서 중간을 구하기 위해 몫을 구한다.
    mid = (start + end)//2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      # 만약 중간값보다 배열의 값이 크다면 좌측으로 옮긴다.
      end = mid - 1
    else: 
      # array[mid] < target
      # 만약 중간값보다 배열의 값이 작다면 우측으로 옮긴다.
      start = mid + 1 
  return None
      
for i in range(8):
  # N_list의 요소들값을 기준으로해서 좌, 우로 움직여가며 탐색을 진행한다.
  # start, end는 아래와 같이 리스트의 처음부터 끝까지로 정해서 시작한다.
  result = binary_search(N_list, M_list[i], 0, N - 1)
  if result is not None:
    print(1, end=' ')
  else:
    print(0, end=' ')