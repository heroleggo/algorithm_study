N = int(input())

for i in range(1, N + 1):
	arr = list(map(int, str(i)))
	if i + sum(arr) == N:
		print(i)
		break
	if i == N:
		print(0)
		break