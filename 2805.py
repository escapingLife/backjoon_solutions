import sys

#정해진 길이인 cut_length로 잘랐을 때 얻는 나무들의 길이 총 합
def sum_cutting_tree_length(cut_length):
    sum_length = sum((length - cut_length)
                     for length in tree_list if length >= cut_length)

    return sum_length

def lower_bound(M):
    # 자르는 길이 < 최대 나무길이
    left, right = 0, max(tree_list)

    #left에서 right까지 검색
    while left <= right:
        mid = (left + right) // 2

        #원하는 길이와 일치할 때 바로 반환.
        if sum_cutting_tree_length(mid) == M :
            return mid
        #잘라진 길이가 많다 = cut_length가 낮다.
        elif sum_cutting_tree_length(mid) > M:
            left = mid + 1
        else:
            right = mid - 1

    #구하고자 하는 left는 길이. 1을 빼준다.
    return left - 1

user_input = sys.stdin.read().strip().splitlines()

N, M = map(int, user_input[0].split())
tree_list = [int(length) for length in user_input[1].split()]

print(lower_bound(M))