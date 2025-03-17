# f(n) = f(n - 1) + f(n - 2) *(n > 2)

def isnt_memorized(memo_list, target):
    return memo_list[target] == 0


def tiling(memo_list, target):
    # 메모이제이션이 안되었을 경우, 반복함수를 사용해 배열을 채움
    if isnt_memorized(memo_list, target):
        # f(n) = f(n - 1) + f(n - 2) *(n > 2)
        for i in range(3, target + 1):
            memo_list[i] = memo_list[i - 1] + memo_list[i - 2]

    return memo_list[target]


n = int(input())

# 0으로 초기화
# n이 1이면 1, n이 2이면 2 n이 0일땐 0으로 임의로 채워넣는다.
memo_list = [0] * 1003
memo_list[1], memo_list[2] = 1, 2

# 10007로 나눈 나머지를 출력한다는 조건
print(tiling(memo_list, n) % 10007)
