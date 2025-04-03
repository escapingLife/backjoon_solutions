import sys
from collections import deque

user_input = sys.stdin.read().strip().splitlines()

n = int(user_input[0])
stack = deque()

#index는 1부터 n까지 숫자중 다음에 선택될 숫자를 고른다.
#target는 입력된 부분인 user_input[1:]에서 다음에 선택될 숫자를 고른다.
index, target = 1, 1
#출력을 저장하는 배열.
print_record = []

#push -> 불가능검사 -> pop순
#불가능은 pop할 때만 발생
while True:
    #출력할 숫자 설정
    target_num = int(user_input[target])

    #1~n 까지 숫자들을 모두 push하지 않을 때 지속적으로 push검사
    if index <= n:
        #push할땐 target까지 있는 숫자를 지속적으로 더한다. index도 증가
        for i in range(index, target_num + 1):
            stack.append(index)
            print_record.append("+")
            index += 1

    #불가능 검사
    #불가능 : 다음에 출력할 숫자가 index보다 작고 스택 맨위 숫자가 아닐때
    #index가 1보다 큰 상태.
    if target_num < (index - 1) and target_num != stack[-1]:
        print("NO")
        break

    #pop
    stack.pop()
    print_record.append("-")
    #다음 출력될 숫자의 위치 설정
    target += 1

    #전부 출력 했을때 기록한 숫자들을 출력.
    if index > n and len(stack) == 0:
        print(*print_record, sep="\n")
        break