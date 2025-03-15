#1 -> 1, 2 -> 2, 3 -> 4 이것들은 기본값.
#규칙 : 4이상의 숫자들은 1 + ?, 2 + ?, 3 + ?으로 분리가능
#?를 메모이제이션으로 저장, (1,2,3 + ?) 의 경우의 수는 ?을  1,2,3의 합으로 나타낸 것과 같다.

#배열 안의 요소가 0이 아니면 전에 메모이제이션이 된 상태
def isnt_memorized(target):
    return memo_list[target] == 0

def separating_1_2_3(target):
    if isnt_memorized(target):
        # (1,2,3 + ?) 의 경우의 수는 ?을  1,2,3의 합으로 나타낸 것과 같다.
        memo_list[target] = (separating_1_2_3(target - 1) +
                             separating_1_2_3(target - 2) +
                             separating_1_2_3(target - 3)
        )

    return memo_list[target]

T = int(input())

#메모이제이션에 쓸 배열을 0으로 초기화
memo_list = [0] * 11

#1 -> 1, 2 -> 2, 3 -> 4세팅
memo_list[0] = 1
memo_list[1] = 2
memo_list[2] = 4

for i in range(T):
    n = int(input())
    # 배열은 0부터 시작이므로 1을 빼준다.
    print(separating_1_2_3(n - 1))
