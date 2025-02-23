# A - Your First Judge
def find_S():
    S = str(input())
    if S == "Hello,World!":
        return "AC"
    else:
        return "WA"
# print(find_S())

# B - Lacked Number
def lacked_number():
    S = str(input())
    numbers = [int(ch) for ch in S]
    for i in range(10):
        if i not in numbers:
            return i
# print(lacked_number())

# C - Minimize Ordering
def minimize_ordering():
    S = str(input())
    chars = list(S)
    chars.sort()
    return ''.join(chars)
# print(minimize_ordering())

# D - Everyone is Friends
def everyone_is_friends():
    N, M = map(int, input().split())
    events = []
    for _ in range(M):
        data = list(map(int, input().split()))
        events.append(set(data[1:]))

    for i in range(1, N):
        for j in range(i + 1, N + 1):
            if not any({i, j}.issubset(event) for event in events):
                return "No"
    return "Yes"
# print(everyone_is_friends())