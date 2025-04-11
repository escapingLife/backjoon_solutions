#인덱스 번호가 5일때 부터, 해당 값은 n - 1값과 n - 5값을 합친것과 같다.
def padovan_sequence(N):
    #메모이 제이션이 되어있는지 확인
    if dp_list[N] == 0:
        dp_list[N] = padovan_sequence(N - 5) + padovan_sequence(N - 1)

    return dp_list[N]


T = int(input())

dp_list = [0] * 100
#기본값 추가
dp_list[0], dp_list[1], dp_list[2] = 1, 1, 1
dp_list[3], dp_list[4] = 2, 2

for _ in range(T):
    N = int(input())

    #1부터 시작하므로 1을 빼준다.
    print(padovan_sequence(N - 1))