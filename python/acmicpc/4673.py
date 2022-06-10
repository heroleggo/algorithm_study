def d(n):
	v = n
	while n != 0:
		v += n % 10
		n //= 10
	return v

result = []

for i in list(range(1, 10001)):
	result.append(d(i))
	if i not in result:
		print(i)