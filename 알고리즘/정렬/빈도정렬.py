import sys
from collections import Counter
n, c = list(map(int,input().split()))
numbers = list(map(int, sys.stdin.readline().split()))
# Counter를 사용한 처리
# 리스트 내부에서 각 숫자들의 순번을 파악하기 위하여,중복된 숫자를 제거하였다.
# 여기서 set을 사용하지 않고 따로 리스트를 만들어서 처리한 이유는
# set은 중복제거 + 자제적으로 sort까지 하기 때문에 내가 원하는 형식인
# 순서는 유지된채 중복만 제거할 수 없기 때문에 아래와 같이 나만의 중복 제거를 처리하였다.
set_numbers = []
[set_numbers.append(x) for x in numbers if x not in set_numbers]

# 마지막은 람다를 사용하여 count되는 숫자가 많은 수를 기준으로 하는 내림차순으로 설정하고,
# 중복을 제거한 리스트를 사용하여 해당 리스트에서 내가 찾고자하는 인자의 index위치를 기준으로 
# 오름차순으로 정렬시켰다.
sorted_list = sorted(numbers, key=lambda x: (-Counter(numbers)[x], set_numbers.index(x)))
print(*sorted_list)