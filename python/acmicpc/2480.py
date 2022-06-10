string = input()

first = int(string.split(' ')[0])
second = int(string.split(' ')[1])
third = int(string.split(' ')[2])

flag = 0

arr = [0,0,0,0,0,0]

arr[first-1] += 1
arr[second-1] += 1
arr[third-1] += 1

for i in range(0, len(arr)):
    if arr[i] == 2:
        print(((i+1) * 100) + 1000)
        break
    elif arr[i] == 3:
        print(((i+1) * 1000) + 10000)
        break
    elif arr[i] == 1:
        flag += 1

if flag == 3:
    if first > second and first > third:
        print(first * 100)
    if second > third and second > first:
        print(second * 100)
    if third > first and third > second:
        print(third * 100)