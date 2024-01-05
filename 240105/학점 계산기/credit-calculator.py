n = int(input())
li = list(map(float, input().split()))

e = len(li)
s = sum(li)
avg = s/e
print(f'{avg:.1f}')

if avg >= 4.0:
    print('Perfect')
elif avg >= 3.0:
    print('Good')
else:
    print('Poor')