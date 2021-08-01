n = int(input())
m = int(input())

a = [int(x) for x in input().split()]
a.sort()
if n == 1:
    print(sum(a))

else:
    n1 = sum(a[:m - 1])
    n2 = a[m - 1]
    flag = 0
    while flag == 0:
        diff = abs(n1 - n2)
        avg = diff // 2

        sl = []
        for i in range(m):
            if a[i] < diff:
                sl.append(a[i])
            else:
                break

        if len(sl) == 0:
            flag = -1
            print(min(n1, n2))
            break

        l = sl[min(range(len(sl)), key=lambda x: abs(sl[x] - avg))]

        if n1 > n2:
            n1 -= l
            n2 += l
        else:
            n1 += l
            n2 -= l
