'''
Counter
* 파이썬 collections 라이브러리의 Counter는 등장 횟수를 세는 기능을 제공
* 리스트와 같은 반복 가능한 객체가 주어졌을 떄 내부의 원소가 몇 번씩 등장했는지 아려줌
'''
from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'])

# 결과 : 2
print(counter['blue'])

# 결과 : 1
print(counter['green'])

# 결과 : {'red': 2, 'blue': 3, 'green': 1}
print(dict(counter))
