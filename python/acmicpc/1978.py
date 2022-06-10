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

N = int(input())

list = map(int, input().split(' '))

answer = 0

for i in list:
	if isPrime(i):
		answer += 1

print(answer)