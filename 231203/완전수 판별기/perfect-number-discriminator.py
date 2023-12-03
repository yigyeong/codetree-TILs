n = int(input())

p= 0
for i in range(1, n//2):
    if n % i == 0:
        p += i

if p == n:
    print('P')
else:
    print("N")