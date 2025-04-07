import sys

input_data = sys.stdin.read().strip().splitlines()

N, M = map(int, input_data[0].split())

vertex = [[] for _ in range(N)]
edge = {}
for i in range(1, 1 + M):
    key, value = map(int, input_data[i].split())

    if key in edge:
        edge[key].append(value)
    edge[key] = [value]

print(edge)