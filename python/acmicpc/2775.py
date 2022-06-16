T = int(input())

data = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14]]

for i in range(1, 15):
	s = []
	for j in range(14):
		su = 0
		for k in range(j+1):
			su += data[i-1][k]
		s.append(su)
	data.append(s)

result = []

for i in range(T):
	k = int(input())
	n = int(input())
	result.append(data[k][n-1])

for i in result:
	print(i)
