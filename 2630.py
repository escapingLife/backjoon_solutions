import sys

#분할된 색종이가 단색인지 구함
def is_one_color(di_p):
    color = di_p[0][0]

    for i in range(len(di_p)):
        for j in range(len(di_p)):
            if not color == di_p[i][j]:
                return False

    return True

def color_count(di_p):
    #단색 색종이가 0을 저장하면 하얀색
    # 0 -> white_count, 1 -> blue_count
    if di_p[0][0] == 0:
        white_blue_list[0] += 1
    else :
        white_blue_list[1] += 1

# di_p = divided_paper
# 단색 색종이일 경우 각 색종이의 개수를 증가시킨다.
# 단색 색종이가 아닐경우 한번더 4등분한다.
def dividing_paper(di_p):
    #길이가 1일경우 재귀를 멈춤, 각 색종이의 개수를 증가시킨다.
    #만약 색종이가 단색일 경우, 재귀를 멈춘다.
    if len(di_p) <= 1 or is_one_color(di_p):
        color_count(di_p)
        return di_p

    length = len(di_p)
    sector_size = length // 2
    #A -> 1, B -> 2, C -> 3, D -> 4
    parts = {
        "A" : [row[0: sector_size] for row in di_p[0: sector_size]],
        "B" : [row[sector_size: length] for row in di_p[0: sector_size]],
        "C" : [row[0: sector_size] for row in di_p[sector_size: length]],
        "D" : [row[sector_size: length] for row in di_p[sector_size: length]]
    }
    #각 부분을 재귀분할 시킴
    for key, value in parts.items():
        dividing_paper(value)

#입력 부분
input_data = sys.stdin.read().strip().splitlines()

N = int(input_data[0])
paper = (
    [list(map(int, line.split())) for line in input_data[1:N + 1]]
)

# 0 -> white_count, 1 -> blue_count
white_blue_list = [0] * 2

dividing_paper(paper)

#색종이 개수를 출력
print(*white_blue_list, sep="\n")