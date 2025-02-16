n = int(input())
a = list(map(int, input().split()))

def card_game_for_two(n, a):
    alice_score = 0
    bob_score = 0
    sorted_a = sorted(a, reverse=True)
    for i in range(n):
        if i % 2 == 0:
            alice_score += sorted_a[i]
        else:
            bob_score += sorted_a[i]
    return alice_score - bob_score

print(card_game_for_two(n, a))