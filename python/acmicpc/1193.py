def sigma(n):
	return n * (n + 1) / 2

N = int(input())

i = 0

while(True):
	if N <= sigma(i):
		x = N - sigma(i-1)
		y = i + 1 - (N - sigma(i-1))
		if (i+1)%2:
			print(str(int(x))+'/'+str(int(y)))
		else:
			print(str(int(y))+'/'+str(int(x)))
		break
	else:
		i += 1