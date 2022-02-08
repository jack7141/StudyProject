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