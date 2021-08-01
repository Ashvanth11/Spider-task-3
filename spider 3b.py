def numofprimes(k):
    num = 0
    prime = [1 for i in range(k + 1)]
    p = 2
    while p * p <= k:

        if prime[p]:

            for i in range(p * 2, n + 1, p):
                prime[i] = 0
        p += 1
    prime[0] = 0
    prime[1] = 0

    for p in range(k + 1):
        if prime[p]:
            num += 1
    return num


n = int(input())
a = numofprimes(n)
ans = a * (a + 1) / 2
print(int(ans))
