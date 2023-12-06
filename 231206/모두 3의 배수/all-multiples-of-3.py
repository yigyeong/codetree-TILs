satisfied = False

for _ in range(5):
    x = int(input())
    if x % 3 != 0:
        satisfied = True

if satisfied == False:
    print(1)
else:
    print(0)