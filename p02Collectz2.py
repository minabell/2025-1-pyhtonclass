# 2025.4.9 우박수 프로젝트 두 번째: 기본 통계량 구하기
# numpy 배열, list 두 가지 방식으로 시험
# 구하는 통계량: 최댓값, 평균, 중앙값, 표준편차, 최빈값

import numpy as np
import statistics
import time

from p02Collatzfunc import collatz

MAXIMUM = 100

# Collatz 수열 길이를 계산하는 함수


# 리스트 방식

start = time.time()
ncountl = []
for n in range(1, MAXIMUM):
    ncountl.append(collatz(n))

print(f'최대값 = {max(ncountl):.5f}')
print(f'평균 = {statistics.mean(ncountl):.5f}')
print(f'중앙값 = {statistics.median(ncountl):.5f}')
print(f'최빈값 = {statistics.mode(ncountl):.5f}')
print(f'표준편차 = {statistics.stdev(ncountl):.5f}')

# numpy 방식
start = time.time()

ncounta = np.zeros(MAXIMUM - 1)
for n in range(1, MAXIMUM):
    ncount = collatz(n)
    ncounta[n - 1] = ncount

print(f'최대값 = {np.max(ncounta):.5f}')
print(f'평균 = {np.mean(ncounta):.5f}')
print(f'중앙값 = {np.median(ncounta):.5f}')
print(f'최빈값 = {np.bincount(ncounta.astype(int)).argmax():.5f}')
print(f'표준편차 = {np.std(ncounta):.5f}')

end = time.time()
print(f'\n⏱ {end - start:.5f} 초가 걸렸습니다')
