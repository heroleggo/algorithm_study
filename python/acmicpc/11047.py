N, K = map(int, input().split(' '))

coins = []
acc = 0

for i in range(N):
	coins.append(int(input()))

coins.sort(reverse=True)

for i in coins:
	acc += int(K / i)
	K = K % i

print(acc)