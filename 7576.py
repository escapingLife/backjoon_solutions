import sys
from collections import deque

UNRIPE = 0
RIPE = 1
BLOCKED = -1    # 막힌 공간

# 마지막에 익지않은 토마토가 없는지 확인
def is_no_empty_slot(count):
    return count == total_unripe_count

# 탐색할 가치가 있는지 확인
def checking_condition(x, y):
    return 0 <= x < M and 0 <= y < N and storage[y][x] == UNRIPE

def BFS():
    # 큐 세팅
    queue = deque()
    ripped_count = 0  # 토마토를 채운 칸의 수
    time_per_day = 0    # 시간 측정 단위
    
    # 익은 토마토 위치를 큐에 삽입
    for x, y in tomato_list_initial_ripe:
        queue.append((x, y, 0)) # x, y, time_per_day

    dy = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dx = [0, 0, -1, 1]  # 상, 하, 좌, 우
    
    # 큐가 빌때 까지 반복
    while queue:
        x, y, time_per_day = queue.popleft()
        
        # 4방향 탐색
        for n_x, n_y in zip(dx, dy):
            next_x = x + n_x
            next_y = y + n_y
            
            if checking_condition(next_x, next_y):
                ripped_count += 1    # 토마토가 익은 갯수 증가
                queue.append((next_x, next_y, time_per_day + 1)) # 시간 증가

                storage[next_y][next_x] = RIPE # 토마토 익음 표시

    # 모든 토마토가 익은 경우
    if is_no_empty_slot(ripped_count):
        return time_per_day
    
    return -1   # 모든 토마토가 익지 않은 경우


# 첫 줄 정보 읽기
M, N = map(int, sys.stdin.readline().split())

storage = []    # 창고의 전체 좌표
tomato_list_initial_ripe = []    # 익은 토마토의 위치
total_unripe_count = 0   # 익지 않은 토마토의 개수

# 세로줄 마다 반복
for r_idx in range(N):
    # 세로 줄 마다 읽기
    current_row = list(map(int, sys.stdin.readline().split()))
    storage.append(current_row)

    # 가로줄 마다 반복
    for c_idx, slot in enumerate(current_row):
        # 익은 토마토 위치 복사
        if slot == RIPE:
            tomato_list_initial_ripe.append([c_idx, r_idx]) # (x좌표, y좌표)
        # 익지 않은 토마토 개수 체크
        elif slot == UNRIPE:
            total_unripe_count += 1

print(BFS())