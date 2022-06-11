N = int(input())

queue = []

size = 0

result = []

idx = 0

for i in range(N):
	command = input().split(' ')
	if command[0] == 'push':
		queue.append(int(command[1]))
		size += 1
	elif command[0] == 'pop':
		if size == 0:
			result.append(-1)
		else:
			result.append(queue[idx])
			idx += 1
			size -= 1
	elif command[0] == 'size':
		result.append(size)
	elif command[0] == 'empty':
		if size == 0:
			result.append(1)
		else:
			result.append(0)
	elif command[0] == 'front':
		if size == 0:
			result.append(-1)
		else:
			result.append(queue[idx])
	elif command[0] == 'back':
		if size == 0:
			result.append(-1)
		else:
			result.append(queue[-1])

for i in result:
	print(i)