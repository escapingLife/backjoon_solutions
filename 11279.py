import sys

#힙이 비었는지 확인한다.
def is_empty():
    return len(max_heap) == 0

#힙 무결성 검사. heap_up기능을 수행한다.
def integrity_check(index):
    parent_index = (index - 1) // 2

    #부모 인덱스가 음수일 때를 제외한다
    #부모가 자식보다 큰 경우 교체한다.
    if parent_index > -1 and max_heap[index] > max_heap[parent_index]:
        max_heap[index], max_heap[parent_index] = max_heap[parent_index], max_heap[index]
        #교환시 부모도 인덱스 검사를 진행함
        integrity_check(parent_index)

#힙 내용 추가
def append(n):
    max_heap.append(n)
    length = len(max_heap)

    #인덱스가 1이상인 경우 무결성 검사
    if length > 1:
        integrity_check(length - 1)

#힙의 맨 마지막 숫자를 루트까지 올린뒤, 무결성 검사를 진행한다.
def heap_down(index):
    left = 2 * index + 1
    right = 2 * index + 2
    big_index = index
    length = len(max_heap)

    if left < length and max_heap[left] > max_heap[big_index]:
        big_index = left

    if right < length and max_heap[right] > max_heap[big_index]:
        big_index = right

    #만약 잎의 내용이 더 큰경우 교체한다.
    if not big_index == index:
        max_heap[big_index], max_heap[index] = max_heap[index], max_heap[big_index]
        #그 다음 자식의 무결성 검사 진행
        heap_down(big_index)

def pop():
    if is_empty():
        print(0)
    else:
        print(max_heap[0])

        temp = max_heap.pop()
        #힙이 비어있으면 추가를 안함
        if not is_empty():
            max_heap[0] = temp

        #무결성 검사
        heap_down(0)

user_input = sys.stdin.read().strip().splitlines()

N = int(user_input[0])
max_heap = []

for num in map(int, user_input[1 :]):
    if num == 0:
        pop()

    else :
        append(num)
