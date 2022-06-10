base = input()

hour = int(base.split(' ')[0])
minute = int(base.split(' ')[1])

value = int(input())

r = (minute + value) % 60

added_hour = (hour + int((minute + value) / 60)) % 24

print(f'{added_hour}'+' '+f'{r}')