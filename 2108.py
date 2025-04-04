import sys
import decimal

#산술평균
def avarage():
    return round(sum(sorted_list) / len(sorted_list))
#중앙값
def median():
    return sorted_list[len(user_input[1:]) // 2]
#최빈값
def mode():
    #최빈값이 몇번 나왔는지
    max_count = max(frequency.values())
    #똑같은 최빈값이 몇개 있는지 확인
    mode_count = sum(1 for count in frequency.values() if count == max_count)

    #mode_count가 2개 이상이면 최빈값이 여러개 존재함
    if mode_count >= 2 :
        #최빈값들의 배열 생성
        mode_list = [num for num, count in frequency.items() if count == max_count]

        # 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
        # 최소값을 딕셔너리에 삭제하고 그 다음 최소값을 출력
        mode_list.remove(min(mode_list))
        return min(mode_list)
    else :
        #max_count를 가진 숫자가 최빈값.
        for num, count in frequency.items():
            if count == max_count:
                return num

#범위
def range():
    return max(sorted_list) - min(sorted_list)

user_input = sys.stdin.read().strip().splitlines()

N = int(user_input[0])
#산술평균, 중앙값, 범위에 사용
sorted_list = sorted(map(int, user_input[1:]))

#최빈값에 사용
frequency = {}
#key : value => number : count
#숫자와 각 숫자의 개수를 딕셔너리에 저장
for num_input in map(int, user_input[1:]) :
    if num_input in frequency :
        frequency[num_input] += 1
    else :
        frequency[num_input] = 1

print(avarage())
print(median())
print(mode())
print(range())