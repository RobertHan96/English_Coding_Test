# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때,
# (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

# case1 : 테이블 위치를 벗어날때 (상/하/좌/우)
# case2 : 벽(0)이라서 갈수 없는 길일때 => 다른 경로 선택 반복문으로 (상/하/좌/우) 확인


from collections import deque

n, m = map(int(input().split()))
a = [list(map(int, list(input()))) for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
q = deque()
check = [[False]*m for _ in range(n)]
dist = [[0]*m for _ in range(n)]

# 시작점
q.append((0, 0))
check[0][0] = True
dist[0][0] = 1

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if check[nx][ny] == False and a[nx][ny] == 1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
                check[nx][ny] = True
