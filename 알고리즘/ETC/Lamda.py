

array = [('A', 501, 'ㄱ'), ('B', 520, 'ㅌ'), ('C', 450, 'ㅁ')]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[2]))


list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = list(map(lambda a,b: a + b, list1, list2))
print(result)