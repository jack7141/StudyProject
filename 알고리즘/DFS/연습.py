'''
1. 아이디어
- 2중 for문 => 값 1 && 방문 x => BFS
- BFS 돌면서 그림 개수 +1, 최대값 갱신

2. 자료구조
- 그래프 전체 지도: int[][]
- 방문 : bool[][]
- Queue(BFS)


입력 
출력

6 5  
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
'''
import sys


# sys를 사용한 인풋이 속도가 훨씬 빠름
input = sys.stdin.readline

# 3 x 3
n, m = map(int, input().split())

'''
3 x 3 행렬 생성
1 1 1 1 
0 1 1 0
1 1 0 0
'''
map = [list(map(int, input().split())) for _ in range(n)]

'''
[False, False, False]
[False, False, False]
[False, False, False]
'''
# 방문 유무 확인
checkpoint = [[False] * m for _ in range(n)]


dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y, x):
    rs = 1
    q = [(y, x)]
    while q:
        ey, ex = q.pop()
        print(f'ey:{ey} ex:{ex}')
        for k in range(4):
            ny = ey + dy[k]
            '''
            ny = 0, 1, 1, -1
            ny = 0, 0, 1, 0
            ny = 0, 0, 1, 0
            '''
            nx = ex + dx[k]
            print(f'ny:{ny} nx:{nx}')

            # 매트릭스 범위안에 있냐?
            if 0 <= ny < n and 0 <= nx < m:
                # 만약 매트릭스의 좌표에서 y,x의 좌표가 1이고 아직 방문을 안했으면?
                if map[ny][nx] == 1 and checkpoint[ny][nx] == False:
                    # 방문했음으로 바꾸고
                    checkpoint[ny][nx] = True
                    # Queue에 입력
                    q.append([ny, nx])
    return rs

# 전체그림횟수
count = 0
# 최대 그림의 크기
max_value = 0
# x
for j in range(n):
    # y
    for i in range(m):
        # 해당 위치의 값이 1이면서 방문을 하지 않았으면?
        if map[j][i] == 1 and checkpoint[j][i] == False:
            # 방문 True로 변경
            checkpoint[j][i] = True
            # 전체 그림 갯수를 +1
            count += 1
            # BFS를 통해서 그림 크기를 구해준다.
            max_value = max(max_value, bfs(j, i))
            # 그 후 최대값 갱신
# print(map)
# print(checkpoint)
print(count)
print(max_value)