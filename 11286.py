import sys

#힙이 비었는지 확인한다.
def is_empty():
    return len(absolute_heap) == 0

#힙 무결성 검사. heap_up기능을 수행한다.
def integrity_check(index):
    parent_index = (index - 1) // 2

    #부모 인덱스가 음수일 때를 제외한다
    if parent_index <= -1:
        return

    #부모가 자식보다 절댓값이 작은 경우 교체한다.
    if abs(absolute_heap[index]) < abs(absolute_heap[parent_index]):
        absolute_heap[index], absolute_heap[parent_index] = absolute_heap[parent_index], absolute_heap[index]
        # 교환시 부모도 인덱스 검사를 진행함
        integrity_check(parent_index)

    #절댓값이 같은경우, 부모가 자식보다 작은 경우 교체한다.
    elif abs(absolute_heap[index]) == abs(absolute_heap[parent_index]) and absolute_heap[index] < absolute_heap[parent_index]:
        absolute_heap[index], absolute_heap[parent_index] = absolute_heap[parent_index], absolute_heap[index]
        # 교환시 부모도 인덱스 검사를 진행함
        integrity_check(parent_index)

#힙 내용 추가
def append(n):
    absolute_heap.append(n)
    length = len(absolute_heap)

    #인덱스가 1이상인 경우 무결성 검사
    if length > 1:
        integrity_check(length - 1)

#힙의 맨 마지막 숫자를 루트까지 올린뒤, 무결성 검사를 진행한다.
def heap_down(index):
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    small_index = index
    
    length = len(absolute_heap)

    if left_index < length:
        if abs(absolute_heap[left_index]) < abs(absolute_heap[small_index]):
            small_index = left_index
        elif abs(absolute_heap[left_index]) == abs(absolute_heap[small_index]) and absolute_heap[left_index] < absolute_heap[small_index]:
            small_index = left_index

    if right_index < length:
        if abs(absolute_heap[right_index]) < abs(absolute_heap[small_index]):
            small_index = right_index
        elif abs(absolute_heap[right_index]) == abs(absolute_heap[small_index]) and absolute_heap[right_index] < absolute_heap[small_index]:
            small_index = right_index

    #만약 잎의 내용의 절댓값이 더 작은경우 교체한다.
    if not small_index == index:
        absolute_heap[small_index], absolute_heap[index] = absolute_heap[index], absolute_heap[small_index]
        #그 다음 자식의 무결성 검사 진행
        heap_down(small_index)


def pop():
    if is_empty():
        print(0)
    else:
        print(absolute_heap[0])

        temp = absolute_heap.pop()
        #힙이 비어있으면 추가를 안함
        if not is_empty():
            absolute_heap[0] = temp

        #무결성 검사
        heap_down(0)

user_input = sys.stdin.read().strip().splitlines()

N = int(user_input[0])
absolute_heap = []

for num in map(int, user_input[1 :]):
    if num == 0:
        pop()

    else :
        append(num)
