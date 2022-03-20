from collections import deque
N, M = map(int,input().split())
k = int(input())

# N x M 방문 유무 확인 행렬 생성
visited = [[-1] * N for _ in range(M)]

count = 0
row = 0 # 행
column = M #열
step = 1 # 한칸씩 이동
column_size = M
row_size = N
search = True
while search:
  if column_size < 1:
    print(0)
    break
  for _ in range(column_size):
    count+=1
    column-=step
    visited[column][row] = count
    if count == k:
      print(row+1,M-column)
      search = False
  column_size -= 1
  for _ in range(row_size-1):
    count += 1
    row+=step
    visited[column][row] = count
    if count == k:
      print(row+1,M-column)
      search = False
  row_size -= 1
  step = -step
    

# 2차원 리스트 출력하기
for line in visited:
    for n in line:
        print('%3d'%n, end = '')
    print()
