a, b = input().split(' ')

maxLength = len(a) if len(a) > len(b) else len(b)

a = a.rjust(maxLength, '0')
b = b.rjust(maxLength, '0')

result = []

up = False
for i in range(maxLength):
	idx = maxLength - i - 1
	v = int(a[idx]) + int(b[idx])
	if up:
		v += 1
		up = False
	if v >= 10:
		result.append(v % 10)
		up = True
	else:
		result.append(v)

if up:
	result.append(1)

result.reverse()

data = "".join(list(map(str, result)))

print(data)