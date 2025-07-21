import sys
from collections import deque
INDEX_LIMIT = 1005

def BFS(graph, node, visited):
    # 큐 구현을 위한 deque 라이브러리 활용
    queue = deque([node])
    # 현재 노드를 방문 처리
    visited[node] = True

    # 큐가 완전히 빌 때까지 반복
    while queue:
        # 큐에 삽입된 순서대로 노드 하나 꺼내기
        v = queue.popleft()

        # 현재 처리 중인 노드에서 방문하지 않은 인접 노드를 모두 큐에 삽입
        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True

# 입력값 받음
input_data = sys.stdin.read().strip().splitlines()
N, M = map(int, input_data[0].split())

# 인접 리스트
graph = [[] for _ in range(INDEX_LIMIT)]
# 노드별로 방문 정보를 리스트로 표현
visited = [False] * INDEX_LIMIT

# 그래프 작성
for i in range(M):
    y, x = map(int, input_data[i + 1].split())
    graph[x].append(y)
    graph[y].append(x)

# 연결 요소의 개수
connected_num = 0

# 정점들을 모두 방문
for i in range(1, N + 1):
    if not visited[i]:
        BFS(graph, i, visited)
        connected_num += 1

print(connected_num)