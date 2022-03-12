# 테스트 케이스 입력
T = int(input())

for _ in range(T):
  # 수첩1 정수 N개만큼 입력, 사용하진 않지만 받아줘야지 에러가 안난다..
  N = int(input())
  # 수첩1에 적어둔 정수 갯수, 
  # 시도해본 결과 List로 처리했을 경우 런타임 오류가 나서 찾아보니, 중복을 제거해서
  # 처리해야한다고한다...
  # 그래서 Set으로 바꿔서 처리했다.
  Note_1 = set(map(int, input().split()))
  
  # 수첩2에 적어둔 정수 갯수, 사용하진 않지만 받아줘야지 에러가 안난다..
  M = int(input())
  # 수첩2 정수 N개만큼 입력
  Note_2 = list(map(int, input().split()))

  #아무래도 이 부분에서 중복이 있거나? 중복된 값을 여러차례 찾아서 시간초과가 나는거같다..
  for N2 in Note_2:
    if N2 in Note_1:
      print(1)
    else:
      print(0)