
# 여기서 입력을 받고
N = int(input())  
List_queue = []  

# 왜 여기서 루프를 돌리지??
for i in range(N):
    # 다시 입력을 받고,,
    IO_input = input()  # 선택

    if IO_input.lower() == 'e':
        if len(List_queue) < 10:
            n = int(input())  # 입력
            List_queue.append(n)
        else:
            print('overflow')

    elif IO_input == 'd':
        if len(List_queue) > 0:
            List_queue.pop(0)
        else:
            print('underflow')
            
    else:
        break
from datetime import date				
print(*List_queue)

"""
3
e
10
e
20
e
30

10 20 30



4
d
e
10
e
20
e
30

underflow
10 20 30
"""