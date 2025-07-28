user_input = input()

weight_list = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]

# 훼손된 숫자 위치
wrong_num_idx = None
sum = 0

for i in range(13):
    if user_input[i] == "*":
        wrong_num_idx = i
    else:
        sum += weight_list[i] * int(user_input[i])

for i in range(10):
    if (sum + weight_list[wrong_num_idx] * i) % 10 == 0:
        print(i)
        break