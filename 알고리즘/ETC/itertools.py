'''
https://docs.python.org/ko/3/library/itertools.html
itertools
############################################################################
순열: 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는것
    * {'A','B','C'}에서 두개를 선택하여 나열하는 경우: 
    = 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'
############################################################################
'''
# 모든 순열 구하기
from itertools import permutations

data = ['A', 'B', 'C']

result = list(permutations(data,3))
# 결과: [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
print(result)

############################################################################
# 모든 순열 구하기(중복허용)
from itertools import product

data = ['A', 'B', 'C']

result = list(product(data, repeat=2))
# 결과: [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
print(result)

############################################################################
'''
조합: 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것
    * {'A','B','C'}에서 순서를 고려하지 않고 2개를 뽑는 경우 
    = 'AB', 'AC', 'BC'
'''
############################################################################
# 모든 조합 구하기
from itertools import combinations

data = ['A', 'B', 'C']

result = list(combinations(data,2))
# 결과: [('A', 'B'), ('A', 'C'), ('B', 'C')]
print(result)

############################################################################
# 모든 조합 구하기(중복허용)
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']


result = list(combinations_with_replacement(data,2))
# 결과: [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
print(result)

############################################################################
# product(iterator1, iterator2, .. , [repeat=1]) :
# 데카르트 곱, 중복된 for문으로 표현 가능
from itertools import product

iterator1 = [1, 2, 3]
iterator2 = ['A', 'B', 'C']

print(list(product(iterator1, iterator2)))
# >>> [(1, 'A'), (1, 'B'), (1, 'C'), (2, 'A'), (2, 'B'), (2, 'C'), (3, 'A'), (3, 'B'), (3, 'C')]

print([(i,j) for i in iterator1 for j in iterator2])
# >>> [(1, 'A'), (1, 'B'), (1, 'C'), (2, 'A'), (2, 'B'), (2, 'C'), (3, 'A'), (3, 'B'), (3, 'C')]
 
############################################################################
#중복 순열(순서 o, 중복 o)
from itertools import product

iterator = ['A','B','C','D','E']

print(list(product(iterator, repeat = 1)))
# >>> [('A',), ('B',), ('C',), ('D',), ('E',)]

print(list(product(iterator, repeat = 2)))
# >>> [
# ('A', 'A'), ('A', 'B'), ('A', 'C'), 
# ('A', 'D'), ('A', 'E'), ('B', 'A'), 
# ('B', 'B'), ('B', 'C'), ('B', 'D'), 
# ('B', 'E'), ('C', 'A'), ('C', 'B'), 
# ('C', 'C'), ('C', 'D'), ('C', 'E'), 
# ('D', 'A'), ('D', 'B'), ('D', 'C'), 
# ('D', 'D'), ('D', 'E'), ('E', 'A'), 
# ('E', 'B'), ('E', 'C'), ('E', 'D'), 
# ('E', 'E')
# ]