#n의 범위가 적어 그냥 순차탐색을 사용
def search_coin(K):
    max_coin = coin_list[0]

    #K의 범위 내에 있는 최댓값을 가진 동전을 찾음
    for i in range(len(coin_list)):
        if coin_list[i] <= K:
            max_coin = coin_list[i]

        if coin_list[i] == K:
            break

    return max_coin

N, K = map(int, input().split())

coin_list = [int(input()) for i in range(N)]
coin_count = 0

#K가 0일시 종료
while True:
    if K <= 0:
        break
    #동전 개수를 구하는 부분
    select_coin = search_coin(K)
    coin_count += (K // select_coin)
    K %= select_coin

print(coin_count)