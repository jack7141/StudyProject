n = int(input())
numbers = list(map(int, input().split()))

# 파이썬dict를 사용해서 key, value를 주고 key값을 찾는 방식으로 접근함
dict_numbers = {index:data for index, data in enumerate(sort_numbers)}

result = []

for num in numbers:
  for key, value in dict_numbers.items():
    if value == num:
      # 내가 찾는 값이 있으면 추가하고, dict에서 삭제해준다.
      # break을 한 이유는 동일한 값이 있을수도 있기 때문에 중첩을 방지하고자 처리함
      result.append(key)
      del dict_numbers[key]
      break
      
# unpacking을 위해서 *를 사용      
print(*result)


#==========================================================================================
#다른사람 풀이
n = int(input())
numbers = list(map(int, input().split()))
sort_numbers = sorted(numbers)
result = []

for index in range(n):
  # 정렬이 된 리스트 내부에서 기존 리스트의 값들의 위치 찾기
  # 즉 정렬된 값 : [1,1,1,3,4,4,6,6] 에서 기존 리스트 [4,1,6,1,3,6,1,4]의 인자값 대입해서
  # 위치를 찾는다.
  
  idx = sort_numbers.index(numbers[index])
  result.append(idx)
  
  # 찾고 난 후에 해당 위치를 다시 찾을수 있으므로 방어적인 코드로 None르로 대체!
  sort_numbers[idx] = None
  
print(*result)