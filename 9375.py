# 전체 경우의 수  = (패션 종류당 옷 개수 + 1)들의 곱 - 1

def calculating(fashionCount):
    result = 1

    for count in fashionCount.values():
        result *= (count + 1)

    return result - 1

T = int(input())

for i in range(T):
    #fashion -> count
    fashionCount = {}

    n = int(input())

    for ii in range(n):
        userInput = input().split()

        key = userInput[1]
        if not key in fashionCount:
            fashionCount[key] = 1
        else:
            fashionCount[key] += 1


    print(calculating(fashionCount))