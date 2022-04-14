
# https://claude-u.tistory.com/151, 위상정렬
import heapq

alphabet_dict ={'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6}

num_problem, num_compare = map(int, input().split())
problem_list = [[] for i in range(num_problem + 1)]
indegree = [0 for i in range(num_problem + 1)]
heap = []
result = []


for i in range(num_compare):
    alphabet = input()
    A, B = alphabet_dict[alphabet[0]], alphabet_dict[alphabet[1]]
    problem_list[A].append(B)
    indegree[B] += 1

for i in range(1, num_problem + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)


while heap:
    temp = heapq.heappop(heap)
    result.append(temp)
    for j in problem_list[temp]:
        indegree[j] -= 1
        if indegree[j] == 0:
            heapq.heappush(heap, j)
          

for i in result:
  for key, value in alphabet_dict.items():
    if value == i:
      print(key, end='')