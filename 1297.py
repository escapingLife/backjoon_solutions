import math

userInput = input()

D, H, W = map(float, userInput.split())

angleRatio = H ** 2 + W ** 2
Ratio = D ** 2 / angleRatio

realH = int(math.sqrt(H ** 2 * Ratio))
realW = int(math.sqrt(W ** 2 * Ratio))

print(realH, realW, sep=' ')