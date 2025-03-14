def reverse(N):
    r = 0
    while N > 0:
        d = N % 10
        r = r * 10 + d
        N = N // 10
    return r

N = int(input())
print(reverse(N))