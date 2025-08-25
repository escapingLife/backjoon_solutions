import sys

def finding_meeting():
    max_count = 1   # 회의는 무조건 한 개가 있음
    previous_end_time = meeting_room_list[0][1] # 첫 회의의 종료시간을 저장

    # 전 회의의 종료시간과 시작시간을 비교.
    for i in range(1, N):
        current_start_time = meeting_room_list[i][0]

        # 시작시간 >= 종료시간.
        if current_start_time >= previous_end_time:
            max_count += 1
            # 종료시간 업데이트
            previous_end_time = meeting_room_list[i][1]

    return max_count


user_input = sys.stdin.read().strip().splitlines()

N = int(user_input[0])

meeting_room_list = [list(map(int, row_str.split())) for row_str in user_input[1:]]
# 종료시간을 첫번째, 시작시간을 두번째 기준으로 삼아서 정렬
meeting_room_list.sort(key=lambda x: (x[1], x[0]))

print(finding_meeting())