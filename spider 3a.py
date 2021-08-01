def sod(d):
    s = 0
    for x in str(d):
        s += int(x)
    return s


n = int(input())
ans = 0
while n >= 10:
    ans += 1
    n = sod(n)

print(ans)
