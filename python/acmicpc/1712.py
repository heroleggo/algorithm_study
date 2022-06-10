# c * n > a + b가 되는 최소 n이 손익분기점이 됨.
data = input().split(' ')
arr = list(map(int, data))

base = arr[0]
cost = arr[1]
price = arr[2]

# B(1개 생산 비용)보다 C(1개 판매가)가 작을 경우
# 무조건 손해를 보는 상황이 발생
if price <= cost:
	print('-1')
else:
	result = int((base) / (price - cost)) + 1
	print(result)