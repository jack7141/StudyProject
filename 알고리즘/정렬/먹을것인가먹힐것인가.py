import sys
import bisect

T = int(sys.stdin.readline())
for _ in range(T):
  AB_Numbers = list(map(int, sys.stdin.readline().split()))
  A = list(map(int, sys.stdin.readline().split()))
  B = list(map(int, sys.stdin.readline().split()))
  sorted_A = sorted(A)
  sorted_B = sorted(B)
  count = 0
  for a in sorted_A:
    # 정렬된 A의 값이 [1,1,3,7,8]
    # 정렬된 B의 값이 [1,3,6]
    # 위와 같이 A,B가 정렬된다. 문제의 핵심은 A의 요소들이 B 리스트 내부에서
    # 어디에 위치할 수 있는가를 기준으로 누적을 해주면된다.
    """
    만약 값이 a의 요소가 1일 경우 B 리스트에서 가장 첫번째에 들어가게 되므로 index의 값은 0을
    반환하게 된다. 
    반면 a의 요소가 8일 경우 B 리스트에서 3번째 포지션을 반환!
    이렇게 되면 자연스럽게 내가 원하는 요소보다 작은 B의 요소들의 숫자를 알게되므로
    누계를 해주면 정답이 된다.
    """
    
    # sorted_B에 정렬되어 삽입될 수 있는 포지션을 반환 
    count+=bisect.bisect_left(sorted_B, a)
  print(count)