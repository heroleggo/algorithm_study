def binarySearch(arr, num, first, last):
	if first >= last:
		return False
	mid = int((first + last) / 2)
	if arr[mid] == num:
		return True
	elif arr[mid] > num:
		return binarySearch(arr, num, first, mid - 1)
	else:
		return binarySearch(arr, num, mid + 1, last)
	return False


N = int(input())
A = list(map(int, input().split(' ')))

M = int(input())
B = list(map(int, input().split(' ')))

sorted_array = sorted(A)

for i in B:
	if binarySearch(sorted_array, i, 0, len(sorted_array)):
		print('1')
	else:
		print('0')