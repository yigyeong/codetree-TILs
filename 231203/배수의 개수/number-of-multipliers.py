cnt3 = 0
cnt5 = 0

for _ in range(10):
    n = int(input())

    if n % 3 == 0:
        cnt3 += 1
    elif n % 5 == 0:
        cnt5 += 1

print(cnt3, cnt5)