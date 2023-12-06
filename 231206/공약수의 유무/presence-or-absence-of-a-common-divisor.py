a, b = map(int, input().split())
satisfied = False

for i in range(a, b+1):
    if 1920 % i and 2880 % i:
        satisfied = True

if satisfied == True:
    print(1)
else:
    print(0)