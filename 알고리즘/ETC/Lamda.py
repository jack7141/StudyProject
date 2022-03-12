

array = [('A', 501, 'ㄱ'), ('B', 520, 'ㅌ'), ('C', 450, 'ㅁ')]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[2]))


list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = list(map(lambda a,b: a + b, list1, list2))
print(result)

'''
* lambda를 통해서 여러개의 조건 정렬도 처리할 수 있다.
'''
# 아래와 같은 리스트가 있을때,
# 두번쨰를 기준으로 오름차순 혹은 내림차순으로 정렬을 하고 싶다면?
example_list = [(0,3),(1,2),(2,7),(3,5),(4,1)]

# 아래와 같이 처리된다.
# >>> [(4,1),(1,2),(0,3),(3,5)(2,7)]
# 만약 여기서 내림차순으로 바꾸고 싶다면?
sort_example_list = sorted(example_list, key=lambda x: x[1])

# 아래와 같이 조건에 '-'를 붙여주면 내림차순으로 정렬할 수 있다.
sort_example_list = sorted(example_list, key=lambda x: -x[1])



# 위의 방식으로 여러가지 조건을 정렬하고 싶다면?
N = int(input())

score = []

for _ in range(N):
    [name, kor, eng, math] = map(str, input().split())
    
    score.append([name, int(kor), int(eng), int(math)])

# x[1]값으로 내림차순으로 정렬!
# x[2]값으로 오름차순으로 정렬!
# x[3]값으로 내림차순으로 정렬!
# x[0]값으로 오름차순으로 정렬!
# 동일한 값도 있을 수 있지만 모든 조건을 순차적으로 처리!
sorted_score = sorted(score, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in sorted_score:
    print(i[0])