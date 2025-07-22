from collections import deque
TARGET_LIMIT = 100000
INDEX_LIMIT = 100001

# 탐색할 가치가 있는지 확인
def CheckingCondition(num):
    return 0 <= num <= TARGET_LIMIT and num_list[num] == -1

def BFS(start):
    # 큐 구현
    queue = deque([start])

    # 큐가 빌 때 까지 반복
    while queue:
        target = queue.popleft()
        # target의 저장된 최소 시간
        current_time = num_list[target]

        # 전부 계산한 경우 탈출
        if target == K:
            return

        # 탐색할 3가지 숫자 리스트
        finding_numbers = [target - 1, target + 1, target * 2]

        for number in finding_numbers:
            if CheckingCondition(number):
                # 탐색해야 하는 경우 해당 숫자의 최소 시간 계산
                num_list[number] = current_time + 1
                # 큐에 삽입
                queue.append(number)

N, K = map(int, input().split())

# 빈 리스트를 -1로 설정
# 최대 길이로 설정 (0 ~ TARGET_LIMIT)
num_list = [-1] * INDEX_LIMIT
# 초기값 설정
num_list[N] = 0

BFS(N)

print(num_list[K])