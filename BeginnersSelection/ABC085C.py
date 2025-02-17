N, Y = map(int, input().split())

def otoshidama(N, Y):
    for a in range(0, N + 1):
        for b in range(0, N+1):
            c = N - (a + b)
            if 0 <= c <= N:
                a_amount = a * 10000
                b_amount = b * 5000
                c_amount = c * 1000
                if a_amount + b_amount + c_amount == Y:
                    pattern = []
                    pattern += [a, b, c]
                    return " ".join(map(str, pattern))
                else:
                    continue
    return "-1 -1 -1"

print(otoshidama(N, Y))