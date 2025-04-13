def calculating_point(N, stair_points):
    #초기값 설정
    dp_list = [0] * (N + 1)
    if N == 1:
        return stair_points[0]

    dp_list[1], dp_list[2] = stair_points[0], stair_points[0] + stair_points[1]

    #N까지 탐색하기 위해 N + 1로 설정
    #계단을 건너 뛰는걸 고려한다. 최댓값은 (2칸전 최댓값 + 현재 칸 점수)와
    #(3칸전 최댓값 + 현재 칸 점수 + 1칸전 점수)의 최댓값 과 같다.
    for i in range(3, N + 1):
        dp_list[i] = max(
            dp_list[i - 2] + stair_points[i - 1],
            dp_list[i - 3] + stair_points[i - 1] + stair_points[i - 2]
        )
    return dp_list[N]

N = int(input())

stair_points = []
for _ in range(N):
    stair_points.append(int(input()))

print(calculating_point(N, stair_points))