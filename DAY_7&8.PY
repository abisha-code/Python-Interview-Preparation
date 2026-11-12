#QN_53
# def square_num(num):
#     return num * num

# num=int(input())
# print(square_num(num))

#QN_54
# def find_max(numbers):
#     largest = numbers[0]
#     for num in numbers:
#         if num > largest:
#             largest = num
#     return largest

# numbers = list(map(int, input().split()))
# print(find_max(numbers))

# #QN_55
# def factorial(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact *= i
#     return fact

# print(factorial(int(input())))

# #QN_56
# def factorial(num):
#base condition
#     if num <= 1:
#         return 1
#     return num * factorial(num - 1)

# print(factorial(int(input())))


# #QN_57
# def fibonacci(n):
#     if n <= 2:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(int(input())))


# #QN_58
# def sum_numbers(num):
#     if num <= 0:
#         return 0
#     return num + sum_numbers(num - 1)

# print(sum_numbers(int(input())))


# #QN_59
# def sum_digits(num):
#     if num == 0:
#         return 0
#     return num % 10 + sum_digits(num // 10)

# print(sum_digits(int(input())))


# #QN_60
# def reverse_string(s):
#     if s == "":
#         return ""
#     return reverse_string(s[1:]) + s[0]

# print(reverse_string(input()))