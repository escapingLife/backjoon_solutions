from collections import deque

#position은 내가 원하는 숫자의 위치를 나타냄
def tracking_position(position):
    #최댓값을 먼저 출력. 큐가 출력될때마다 count증가
    num_max = max(num_queue)
    count = 0

    while True:
        #다음으로 출력할 숫자를 구함
        next = num_queue[0]

        #next가 내가 원하는 숫자일때 & next가 큐의 최댓값일때
        if position == 0 and next == num_max:
            count += 1
            break
        #최댓값을 먼저 출력. 출력될때 마다 count는 1증가
        elif next == num_max:
            num_queue.popleft()
            num_max = max(num_queue)
            count += 1
        #처음 요소를 뒤로 삽입
        else:
            num_queue.rotate(-1)

        #position이 큐 맨뒤로 갈때 큐 맨뒤로 위치를 설정
        if (position - 1) < 0:
            position = len(num_queue) - 1
        else :
            position -= 1

    return count

attempt = int(input())

for _ in range(attempt):
    N, M = map(int, input().split())
    num_queue = deque(map(int, input().split()))

    print(tracking_position(M))