# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(input())
List_queue = []

for i in range(user_input):
	IO_input = input()
	if IO_input.lower() == 'e':
		if len(List_queue) < 10:
			number = int(input())
			List_queue.append(number)
		else:
			print('overflow')
	
	elif IO_input.lower() == 'd':
		if len(List_queue) > 0:
			List_queue.pop(0)
		else:
			print('underflow')
	

	else:
		break
		
print(*List_queue)