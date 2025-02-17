def otoshidama(N, Y):
    for a in range(N + 1):
        for b in range(N - a + 1):  # bの範囲を狭める
            c = N - (a + b)
            if a * 10000 + b * 5000 + c * 1000 == Y:
                return f"{a} {b} {c}"
    return "-1 -1 -1"

N, Y = map(int, input().split())
print(otoshidama(N, Y))