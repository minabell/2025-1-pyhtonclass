maxvalue = 0
maxvaluen = 0

for n in range(1, 100):
    #print(f'{n=}')
    ncount = 0

    while n!= 1:
        if n% 2 == 1:
            n = 3 * n + 1
        else:
            n = n / 2
        ncount += 1

    print(f'{ncount}')

    if maxvalue < ncount:
        maxvalue = ncount
        maxvaluen = n

print(f'{maxvalue=}, {maxvaluen=}')
#두번째 큰 값을 찾는 파이썬 프로그램
maxvalue = 0
maxvaluen = 0
secondvalue = 0
secondn = 0

for start_n in range(1, 100):
    n = start_n
    ncount = 0

    while n != 1:
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2
        ncount += 1

    if ncount > maxvalue:
        secondvalue = maxvalue
        secondn = maxvaluen

        maxvalue = ncount
        maxvaluen = start_n
    elif ncount > secondvalue:
        secondvalue = ncount
        secondn = start_n

print(f'2등: {secondn} → {secondvalue}번')
thirdvalue = 0
thirdn = 0

first = 0
second = 0

for start_n in range(1, 100):
    n = start_n
    ncount = 0

    while n != 1:
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2
        ncount += 1

    if ncount > first:
        thirdvalue = second
        thirdn = secondn if 'secondn' in locals() else 0
        second = first
        secondn = start_n
        first = ncount

    elif ncount > second:
        thirdvalue = second
        thirdn = secondn
        second = ncount
        secondn = start_n

    elif ncount > thirdvalue:
        thirdvalue = ncount
        thirdn = start_n

print(f'3등: {thirdn} → {thirdvalue}번')



