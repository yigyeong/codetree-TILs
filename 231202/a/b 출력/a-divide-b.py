a, b = map(int, input().split())

result = a//b
print(f"{result}.", end="")

for i in range(20):
    if a % b == 0:
        print(0, end='')
    else:
        result = (a % b)*10 // b
        print(result, end='')
        a = ((a % b) * 10) % b