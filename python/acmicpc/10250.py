T = int(input())

result = []

for i in range(T):
	H, W, N = map(int, input().split(' '))
	N = N - 1
	targetFloor = (N % H) + 1
	targetRoomNum = int(N / H) + 1
	result.append(str(targetFloor)+str(targetRoomNum).rjust(2, '0'))

for i in result:
	print(i)