# Emma is playing a new mobile game that starts with consecutively numbered clouds.
# Some of the clouds are thunderheads and others are cumulus.
# She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2.
# She must avoid the thunderheads.
# Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud.
# It is always possible to win the game.

# 현재 위치에서 1칸 or 2칸 앞에 적락운이 있는 경우, 그 다음 칸으로 점프가 가능할때
# 시작 위치부터 끝 위치까지 가는데 필요한 최소한의 점프 횟수 반환

test = [0, 0, 1, 0, 0, 1, 0]
test2 = [0, 0, 0, 0, 1, 0]
test3 = [0, 1, 0, 1, 0, 0]

# 현재 위치에서 1, 2 칸 뒤에 값 검사
# 적락운이라면 1, 2칸 뒤에 값, 다음 값이 0이 아닐 경우 점프 진행
# 마지막 값은 항상 적란운이 없기때문에 거기까지는 검사하지 않아도 됨


def jumpingOnClouds(c):
    if len(c) == 1:
        return 0
    if len(c) == 2:
        return 0 if c[1] == 1 else 1
    if c[2] == 1:
        return 1 + jumpingOnClouds(c[1:])
    if c[2] == 0:
        return 1 + jumpingOnClouds(c[2:])


print(jumpingOnClouds(test))
