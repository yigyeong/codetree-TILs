n = int(input())
prod = []
cnt = 0

for i in range(1, 11):
    prod.append(i*n)
    if i*n % 5 == 0:
        cnt += 1
    if cnt == 2:
        break

print(*prod)