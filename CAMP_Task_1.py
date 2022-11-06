import numpy as np
import math

R = float(input("R = "))
MaxPointNum = 300000

num = 0
for i in range(MaxPointNum):
    x = np.random.uniform(-R, R)
    y = np.random.uniform(-R, R)
    if math.sqrt(math.pow(x,2) + math.pow(y,2)) <= R:
        num += 1

Pi = (num / MaxPointNum)*4

print("Pi = ", Pi)