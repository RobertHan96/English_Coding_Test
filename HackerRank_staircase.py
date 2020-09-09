sharp = 1


def staircase(n):
    global sharp
    for i in range(n):
        for j in range(n+1):
            if j == n:
                print(end='\n')
                sharp += 1
            elif j < n and j + sharp < n:
                print(' ', end='')
            else:
                print('#', end='')


staircase(100)
