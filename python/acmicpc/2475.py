inp = input() # '1 2 3 4 5'의 형태

arr = inp.split(' ')

value = 0
for i in arr:
	value += (int(i) ** 2)

print (value % 10)
