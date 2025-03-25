from collections import deque

def BFS(start):
    #방향지정
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])

    while queue:
        x, y = queue.popleft()

        check_list.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            #nx, ny가 범위를 넘어가지 않는지 확인
            if 0 <= nx < len(ground) and 0 <= ny < len(ground[0]):
                if (nx, ny) not in check_list and ground[nx][ny] == 1:
                    queue.append((nx, ny))
                    check_list.add((nx, ny))

T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())

    ground = [[0] * M for _ in range(N)]
    check_list = set()

    for _ in range(K):
        # x, y입력후 1로 저장
        x, y = map(int, input().split())
        ground[y][x] = 1

    worm_count = 0
    for j in range(N):
        for k in range(M):
            if ground[j][k] == 1 and (j, k) not in check_list:
                BFS((j, k))
                worm_count += 1

    print(worm_count)