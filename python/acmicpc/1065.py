def check(n):
	ret = 0
	s = str(n)
	if len(s) <= 2:
		ret += n
	else:
		ret += 99
		for i in range(100, n+1):
			t = str(i)
			if (ord(t[0]) - ord(t[1])) == (ord(t[1]) - ord(t[2])):
				ret += 1
	return ret

v = int(input())

print(check(v))