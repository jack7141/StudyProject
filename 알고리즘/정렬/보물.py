# 두번째 리스트는 재배열하면 안되는 거였다.....!!!)ㅠㅠㅠㅠㅠㅠㅠ 문제를 너무 대충 읽었다,..,ㅠ

n = int(input())
numbers = list(map(int, input().split()))
numbers_2 = list(map(int, input().split()))

# 두 리스트의 합을 비교했을때 리스트의 크기가 큰 리스트를 찾는다
# (A>B) - (A<B) => A를 기준으로 A보다 B가 크면! 음수, 같으면 0 A가 크면 양수를 리턴한다.
compare_AB = (sum(numbers) > sum(numbers_2)) - (sum(numbers) < sum(numbers_2))


def mutipleList(descending, ascending):
  result = 0
  # Zip을 통해서 두개의 리스트를 곱해서 누적한 후 리턴!
  for a, b in zip(descending, ascending):
    result += a*b
  return result

if compare_AB == -1:  
  # 첫번째 리스트가 두번째 리스트의 합보다 작은 경우! 
  # 첫번째 리스트를 오름차순으로, 두번째 리스트를 내림차순으로 정렬!
  descending = sorted(numbers)
  ascending = sorted(numbers_2,reverse=True)
  
  print(mutipleList(descending, ascending))
  
elif compare_AB == 1:
  # 첫번째 리스트가 두번째 리스트의 합보다 큰 경우! 
  # 첫번째 리스트를 내림차순으로, 두번째 리스트를 오름차순으로 정렬!
  descending = sorted(numbers_2)
  ascending = sorted(numbers,reverse=True)
  print(mutipleList(descending, ascending))
else:
  # 첫번째 리스트와 두번째 리스트의 합이 동일할 경우 두 리스트중 가장 큰 값을 비교해서
  # 가장 큰 값이 있는 리스트를 내림차순으로 그게 아닌 리스트를 오름차순으로
  if max(numbers) < max(numbers_2):
      descending = sorted(numbers)
      ascending = sorted(numbers_2,reverse=True)
      print(mutipleList(descending, ascending))
  else:
    descending = sorted(numbers_2)
    ascending = sorted(numbers,reverse=True)
    print(mutipleList(descending, ascending))

# 출제자 의도에 맞는 올바른 풀이
n = int(input())
numbers = list(map(int, input().split()))
number_2 = list(map(int, input().split()))
numbers.sort()

result = 0

for i in range(n):
  # x의 값은 위에서 이미 sort를 통해서 정렬을 했기 때문에 맨 앞쪽부터 계산해 나가면 된다.
  x = numbers[i]
  
  # 두번째 리스트 값중 가장 큰값의 index를 찾아서 pop시키고 두 값을 곱해준다.
  y = numbers_2.pop(numbers_2.index(max(numbers_2)))
  
  result += x * y
  
print(result)