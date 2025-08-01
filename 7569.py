import sys
from collections import deque

UNRIPE = 0
RIPE = 1
BLOCKED = -1  # 막힌 공간

# 마지막에 익지않은 토마토가 없는지 확인
def is_no_empty_slot(count):
    return count == total_unripe_count


# 탐색할 가치가 있는지 확인
def checking_condition(x, y, z):
    return 0 <= x < M and 0 <= y < N and 0 <= z < H and storage[z][y][x] == UNRIPE


def BFS():
    # 큐 세팅
    queue = deque()
    ripped_count = 0  # 토마토를 채운 칸의 수
    time_per_day = 0  # 시간 측정 단위

    # 익은 토마토 위치를 큐에 삽입
    for x, y, z in tomato_list_initial_ripe:
        queue.append((x, y, z, 0))  # x, y, z, time_per_day

    dx = [0, 0, -1, 1, 0, 0]    # 상, 하, 좌, 우, 위, 아래
    dy = [-1, 1, 0, 0, 0, 0]    # 상, 하, 좌, 우, 위, 아래
    dz = [0, 0, 0, 0, 1, -1]    # 상, 하, 좌, 우, 위, 아래

    # 큐가 빌때 까지 반복
    while queue:
        x, y, z, time_per_day = queue.popleft()

        # 4방향 탐색
        for n_x, n_y, n_z in zip(dx, dy, dz):
            next_x = x + n_x
            next_y = y + n_y
            next_z = z + n_z

            if checking_condition(next_x, next_y, next_z):
                ripped_count += 1  # 토마토가 익은 갯수 증가
                queue.append((next_x, next_y, next_z, time_per_day + 1))  # 시간 증가

                storage[next_z][next_y][next_x] = RIPE  # 토마토 익음 표시

    # 모든 토마토가 익은 경우
    if is_no_empty_slot(ripped_count):
        return time_per_day

    return -1  # 모든 토마토가 익지 않은 경우

M, N, H = map(int, sys.stdin.readline().split())    # 첫 줄 읽기

storage = []  # 창고의 전체 좌표, storage[z][y][x]
tomato_list_initial_ripe = []  # 익은 토마토의 위치
total_unripe_count = 0  # 익지 않은 토마토의 개수

# 층 마다 반복
for h_idx in range(H):
    layer = []

    # 세로줄 마다 반복
    for r_idx in range(N):
        # 한 줄 씩 읽기
        current_row = list(map(int, sys.stdin.readline().split()))
        layer.append(current_row)  # 현재 층에 줄 추가

        # 가로줄 마다 반복
        for c_idx, slot in enumerate(current_row):
            # 익은 토마토 위치 복사
            if slot == RIPE:
                tomato_list_initial_ripe.append([c_idx, r_idx, h_idx])  # (x, y, z)
            # 익지 않은 토마토 개수 체크
            elif slot == UNRIPE:
                total_unripe_count += 1

    storage.append(layer) # 층 마다 입력

print(BFS())