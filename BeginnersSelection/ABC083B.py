n, a, b = map(int, input().split())

def count_int_between_a_and_b(n, a, b):
  ans = 0
  for i in range(a, n + 1):
    summed_numbers = sum_all_numbers(i)
    if a <= summed_numbers <= b:
      ans += i
  return ans

def sum_all_numbers(n):
  ans = sum(map(int, str(n)))
  return ans

print(count_int_between_a_and_b(n, a, b))