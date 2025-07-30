# r_idx, c_idx는 쪼갠 사각형의 첫번째 칸을 알려주는 인덱스 번호
def Z(r_idx, c_idx, target_r, target_c, N):
    # 더이상 쪼갤수 없을 때 재귀형 탐색 종료
    if N <= 0:
        return 0

    half_idx =  int(pow(2, N)) // 2     # 4등분 했을 떄, 증가 되는 인덱스 양
    half_amount = int(pow(4, N - 1))    # 4등분 했을 때, 증가 되는 count 양

    # 순서        0      1            2                3
    dy =        [0,     0,           half_idx,        half_idx]
    dx =        [0,     half_idx,    0,               half_idx]
    d_amount =  [0,     half_amount, half_amount * 2, half_amount * 3]

    # 순서 찾기
    for r, c, amount in zip(dy, dx, d_amount):
        n_r = r + r_idx
        n_c = c + c_idx

        # target가 순서 0 ~ 3중 어디에 속해있는 지 파악
        if (n_r <= target_r < n_r + half_idx) and (n_c <= target_c < n_c + half_idx):
            # 다음 탐색 + d_amount
            return Z(r_idx + r, c_idx + c, target_r, target_c, N - 1) + amount

    return -1   # 디버깅

N, r, c = map(int, input().split())

print(Z(0, 0, r, c, N))