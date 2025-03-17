import sys

#모든 입력을 읽음, 양쪽끝에 공백 제고, 줄단위로 나누어 리스트로 반환
input_data = sys.stdin.read().strip().splitlines()

N, M = map(int, input_data[0].split())

#숫자가 키일 경우
num_dictionary = {}
#이름이 키일 경우
name_dictionary = {}

for i in range (1, N + 1):
    userInput = input_data[i]
    num_dictionary[i] = userInput
    name_dictionary[userInput] = i

for i in range (N + 1, N + M + 1):
    userInput = input_data[i]

    #userInput이 숫자일 경우
    if userInput.isdigit():
        print(num_dictionary[int(userInput)])
    else:
        print(name_dictionary[userInput])
