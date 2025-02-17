def list_input(n):
    array = []
    for i in range(n):
        array.append(int(input()))
    return array

n = int(input())
d = list_input(n)

def kagami_mochi(d):
    new_array = set(d)
    return len(new_array)

print(kagami_mochi(d))
