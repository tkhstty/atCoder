def can_go_there(time_tables):
    prev_t, prev_x, prev_y = 0, 0, 0
    for t, x, y in time_tables:
        dt = t - prev_t
        dist = abs(x - prev_x) + abs(y - prev_y)

        if dist > dt or (dt - dist) % 2 != 0:
            return "No"

        prev_t, prev_x, prev_y = t, x, y

    return "Yes"

N = int(input())
time_tables = [tuple(map(int, input().split())) for _ in range(N)]
print(can_go_there(time_tables))