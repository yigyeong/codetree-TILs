while True:
    n = int(input())

    if n < 25:
        print('Higher')
    elif n > 25:
        print('Lower')
    if n == 25:
        print('Good')
        break