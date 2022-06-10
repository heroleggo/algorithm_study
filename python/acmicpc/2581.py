import math

def isPrime(n):
	if n == 1:
		return False
	elif n == 2:
		return True
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

m = int(input())
n = int(input())

acc = 0
minimum = 0

for i in range(m, n + 1):
	if isPrime(i):
		if acc == 0:
			minimum = i
		acc += i

if acc == 0:
	print(-1)
else:
	print(acc)
	print(minimum)