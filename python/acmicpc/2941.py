arr = ['c=','c-','dz=','d-','lj','nj','s=','z=']

v = input()

for i in arr:
	v = v.replace(i, '?')

print(len(v))