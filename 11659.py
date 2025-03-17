import sys

input_data = sys.stdin.read().strip().splitlines()

N, M = map(int, input_data[0].split())

num_list = list(map(int, input_data[1].split()))

#각 인덱스 까지 누적합 구하기
#0인 경우엔 직접 삽입 S(0) = 0
pre_sum = [0]
for i in range(N):
    #1부터 S(i + 1) = S(i) + N(i)
    pre_sum.append(num_list[i] + pre_sum[i])

for k in range (2, M + 2) :
    i, j = map(int, input_data[k].split())
    #1부터 5까지인 경우, S(5) - S(0).
    print(pre_sum[j] - pre_sum[i - 1])

