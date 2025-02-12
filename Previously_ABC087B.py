# count = 0
# length = int(input())
# numbers = []

# def is_all_even(numbers):
#     for number in numbers:
#         if number % 2 == 1:
#             print("An odd number was found. Calculation is done.")
#             return False
#     return True

# while is_all_even(numbers):
#     numbers = [number // 2 for number in numbers]  # 整数除算を使用
#     count += 1

# print(count)

def find_min_number_of_palindromes():
  for i in range(10, 1000):
    decimal_number = i
    binary_number = bin(decimal_number)[2:]
    octal_number = oct(decimal_number)[2:]

    if str(decimal_number) == str(decimal_number)[::-1] and binary_number == binary_number[::-1] and octal_number == octal_number[::-1]:
      return decimal_number


def find_reversible_numbers():
  options = ["", '+', '-', '*', '/']
  reversible_numbers = []

  for i in range(1000, 9999):
    i_str = str(i)
    for j in range(4):
      for k in range(4):
        for l in range(4):
          if j+k+l == 0:
            break
          formula = i_str[0] + options[j] + i_str[1] + options[k] + i_str[2] + options[l] + i_str[3]
          if '//' in formula or '/0' in formula:
            continue
          try:
            if str(eval(formula)) == i_str[::-1]:
                reversible_numbers.append(i)
                break
          except ZeroDivisionError:
            continue
          except SyntaxError:
            continue

  return reversible_numbers


def list_of_all_face_down_numbers():
  numbers = [False] * 100

  for i in range(2, 101):
    j = i - 1
    while j < 100:
      numbers[j] = not numbers[j]
      j += i

  face_down_numbers = [i + 1 for i, number in enumerate(numbers) if not number]
  return face_down_numbers


def count_times_to_cut_stick_to_1cm(m, n, current):
  if current >= n:
    return 0
  if current < m:
    return 1 + count_times_to_cut_stick_to_1cm(m, n, current * 2)
  else:
    return 1 + count_times_to_cut_stick_to_1cm(m, n, current + m)


def pattern_of_money_exchange(amount):
  pattern = 0
  for i in range(amount // 10 + 1):
    for j in range(amount // 50 + 1):
      for k in range(amount // 100 + 1):
        for l in range(amount // 500 + 1):
          if i * 10 + j * 50 + k * 100 + l * 500 == amount:
            if i + j + k + l <= 15:
              pattern += 1
  return pattern


a = int(input())
b = int(input())
c = int(input())
x = int(input())

def count_patterns_of_coins_for_amount(a, b, c, x):
  pattern = 0
  # a, b, cの組み合わせでxを作る
  # a, b, cはそれぞれ500円, 100円, 50円の上限枚数
  for i in range(a + 1):
    for j in range(b + 1):
      for k in range(c + 1):
        if i * 500 + j * 100 + k * 50 == x:
          pattern += 1
  return pattern

print(count_patterns_of_coins_for_amount(a, b, c, x))