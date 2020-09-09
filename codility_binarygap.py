test = 1041


def solution(N):
    N = bin(int(N))[2:]
    gap = [0] * len(N)
    temp = 0
    gap[0] = 1
    if N.count('1') < 2:
        return 0

    for i in range(1, len(N)):
        if N[i] == '1':
            temp = 1
            gap[i] = 0
        else:
            if gap[i-1] != 0:
                gap[i] = gap[i-1] + 1
    return max(gap) - 1


print(solution(32))


def best_solution(N):
    return len(max(bin(N)[2:].strip('0').strip('1').split('1')))


t1 = bin(1041)[2:]
t2 = t1.strip('0')
t3 = t2.strip('1')
t4 = t3.split('1')
final = len(max(t4))

print(t1, t2, t3, t4, final)
