n =1
result = 1

while n <= 100:
    a  =((2 * n + 1)**2 -1) / ((2 * n + 1)**2)
    result = result * a
    n = n + 1
print(result*4)

#기본계산
n = 1
p = 1
p = p*((2 * n + 1)**2 -1) / ((2 * n + 1)**2)

n = 2
p = p*((2 * n + 1)**2 -1) / ((2 * n + 1)**2)
print(p*4)

#루프로 변환
p=1
for n in range(1,10):
    p = p * ((2 * n + 1) ** 2 - 1) / ((2 * n + 1) ** 2)

print(p*4)

import matplotlib.pyplot as plt
plt.plot([1,3,4])
plt.show()

import opency