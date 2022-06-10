def check(data):

	charset = []

	l = list(data)
	for i in range(len(l)):
		if data[i] not in charset:
			charset.append(data[i])
		elif data[i] == data[i - 1]:
			continue
		else:
			return False
	return True

n = int(input())

acc = 0

for i in range(n):
	word = input()
	if (check(word)):
		acc += 1

print(acc)