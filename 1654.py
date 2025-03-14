#잘라야 하는 랜선 길이 <= 최대 랜선 길이
#1부터 (최대 랜선 길이 + 1) 사이의 숫자를 이분 탐색(상한)으로 검색함.
#최대 랜선 길이에 1을 더하면 탐색시 최대 랜선 길이를 포함해 탐색 가능

#잘랐을 때 총 랜선 개수를 구함
def get_cut_count(lan_list, lan_cut_size):
    cut_lan_count = 0

    for lan in lan_list:
        # 총 랜선 개수 획득
        cut_lan_count += lan // lan_cut_size

    return cut_lan_count

def upper_bound(lan_list, end, N):
    left, right = 0, end

    while left < right:
        mid = (left + right) // 2

        #만약 자른 개수가 N보다 작을 경우 자르는 길이를 줄여야함.
        if get_cut_count(lan_list, mid) >= N:
            left = mid + 1
        else:
            right = mid

    #실제 길이 반환
    return left - 1

#입력부분
userInput = input()

K, N = map(int, userInput.split())
lan_list = []

for i in range(K):
    lan_list.append(int(input()))

real_lan_length = upper_bound(lan_list, max(lan_list) + 1, N)
print(real_lan_length)