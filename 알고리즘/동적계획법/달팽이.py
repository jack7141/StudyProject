# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = list(map(int,input().split()))

H, U, D, F = user_input

dp = [0]*100
dp[0] = 0
dp[1] = dp[0]+U-D

i = 2
while True:
	dp[i] = dp[i-1] + (U - (U*(F/100))*(i-1)) - D
	if dp[i-1] + (U - (U*(F/100))*(i-1)) > H:
		print(f'Success {i}')
		break
	elif dp[i] < 0 or dp[i-1] + (U - (U*(10/100))*(i-1)) < 0:
		print(f'Failure {i}')
		break
	i += 1