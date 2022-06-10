A, B, V = list(map(int,input().split(' ')))

count = 1

count += int((V-A)/(A-B))
if (V-A)%(A-B):
	count += 1

print(count)