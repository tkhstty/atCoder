# A - When?
def when_the_time():
    K = int(input())
    base_hour = 21
    base_minute = 0
    plus_hour = K // 60
    plus_minute = K % 60
    new_hour = str(base_hour + plus_hour)
    new_minute = str(base_minute + plus_minute)
    padded_minute = new_minute.zfill(2)
    return new_hour + ":" + padded_minute
# print(when_the_time())


# B - New Scheme
def new_scheme():
    S = list(map(int, input().split()))
    for i in range(len(S)-1):
        if S[i] > S[i+1]:
            return "No"
    for i in range(len(S)):
        if S[i] % 25 != 0:
            return "No"
    if max(S) > 675:
        return "No"
    if min(S) < 100:
        return "No"
    return "Yes"
# print(new_scheme())


# C - Failing Grade
def failing_grade():
    N, P = map(int, input().split())
    a = list(map(int, input().split()))
    failed = [i for i in a if i < P]
    return len(failed)
# print(failing_grade())


# D - Enlarged Checker Board
def enlarged_checker_board():
    N, A, B = map(int, input().split())
print(enlarged_checker_board())