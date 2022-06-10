def sigma(n):
	return n * (n + 1) / 2

N = int(input())

val = (N - 1) / 6

i = 1

while(True):
	if val == 0:
		print(1)
		break
	if val <= sigma(i):
		print(i+1)
		break
	else:
		i += 1