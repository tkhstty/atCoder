def hakuchumu(S):
    words = ["eraser", "dreamer", "dream", "erase"]
    while S:
        for word in words:
            if S.endswith(word):
                S = S[: -len(word)]
                break
        else:
            return "NO"
    return "YES"

S = str(input())
print(hakuchumu(S))