def calculate(num):
	i = 2
	while(num != 1):
		if num % i == 0:
			num = num / i
			print(i)
		else:
			i += 1

n = int(input())

calculate(n)