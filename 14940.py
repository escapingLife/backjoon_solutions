import sys
from collections import deque, namedtuple

# 계산한 x, y좌표가 배열의 범위에 벗어나는 지 확인
def check_out_of_boundary(x, y):
    return 0 <= x < m and 0 <= y < n

def BFS(start_x, start_y):
    # 큐 구현
    queue = deque([(start_x, start_y, 1)]) # x좌표, y좌표, 거리

    # 큐가 빌 때 까지 반복
    while queue:
        x, y, distance = queue.popleft()

        # up, down, left, right
        next_ground = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]

        for next_x, next_y in next_ground:
            # 범위 안에 드는지 체크하고, 방문 안한 곳(벽도 아닌 곳)인지 확인
            if check_out_of_boundary(next_x, next_y) and result_map[next_y][next_x] == -1:
                result_map[next_y][next_x] = distance
                queue.append((next_x, next_y, distance + 1))

user_input = sys.stdin.read().strip().splitlines()

n, m = map(int, user_input[0].split())
number_map = [] # 입력 지도

Point = namedtuple('Point', ['x', 'y']) # 좌표 가독성 높이기
start_pt = None   # 시작 지점
# 도달할 수 없는 위치는 자동으로 -1이 됨
result_map = [[-1] * m for _ in range(n)] # 출력 지도

# 지도 채우기
for r_idx, line_str in enumerate(user_input[1:]):
    current_row = list(map(int, line_str.split()))
    number_map.append(current_row)

    for c_idx, num in enumerate(current_row):
        if num == 2:    # 목표지점 찾기
            start_pt = Point(x = c_idx, y = r_idx)   # (x 좌표, y 좌표)
        elif num == 0:  # 벽 입력
            result_map[r_idx][c_idx] = 0

result_map[start_pt.y][start_pt.x] = 0  # 목표지점 표시

BFS(start_pt.x, start_pt.y)

for r_idx in result_map:
    for num in r_idx:
        print(num, end=" ")

    print()