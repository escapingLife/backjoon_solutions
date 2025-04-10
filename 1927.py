import sys

#힙이 비었는지 확인한다.
def is_empty():
    return len(min_heap) == 0

#힙 무결성 검사. heap_up기능을 수행한다.
def integrity_check(index):
    parent_index = (index - 1) // 2

    #부모 인덱스가 음수일 때를 제외한다
    #부모가 자식보다 작은 경우 교체한다.
    if parent_index > -1 and min_heap[index] < min_heap[parent_index]:
        min_heap[index], min_heap[parent_index] = min_heap[parent_index], min_heap[index]
        #교환시 부모도 인덱스 검사를 진행함
        integrity_check(parent_index)

#힙 내용 추가
def append(n):
    min_heap.append(n)
    length = len(min_heap)

    #인덱스가 1이상인 경우 무결성 검사
    if length > 1:
        integrity_check(length - 1)

#힙의 맨 마지막 숫자를 루트까지 올린뒤, 무결성 검사를 진행한다.
def heap_down(index):
    left = 2 * index + 1
    right = 2 * index + 2
    small_index = index
    length = len(min_heap)

    if left < length and min_heap[left] < min_heap[small_index]:
        small_index = left

    if right < length and min_heap[right] < min_heap[small_index]:
        small_index = right

    #만약 잎의 내용이 더 작은경우 교체한다.
    if not small_index == index:
        min_heap[small_index], min_heap[index] = min_heap[index], min_heap[small_index]
        #그 다음 자식의 무결성 검사 진행
        heap_down(small_index)


def pop():
    if is_empty():
        print(0)
    else:
        print(min_heap[0])

        temp = min_heap.pop()
        #힙이 비어있으면 추가를 안함
        if not is_empty():
            min_heap[0] = temp

        #무결성 검사
        heap_down(0)

user_input = sys.stdin.read().strip().splitlines()

N = int(user_input[0])
min_heap = []

for num in map(int, user_input[1 :]):
    if num == 0:
        pop()

    else :
        append(num)
