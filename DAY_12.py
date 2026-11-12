
#QN_151
# nums=list(map(int,input().split()))

# squares=[num**2 for num in nums]
# even_numbers=[num for num in nums if num%2==0]

# print("Squares:", squares)
# print("Even numbers:", even_numbers)


# #QN_152
# nums = list(map(int, input().split()))

# if nums == nums[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


#QN_153
# def flatten(nums):
#     result = []

#     for item in nums:
#         if isinstance(item, list):
#             result.extend(flatten(item))
#         else:
#             result.append(item)
#     return result

# If the item is a list:
# 1. Call the same function recursively.
# 2. Flatten that nested list.
# 3. Add its individual elements to result using extend().




# nums = [1, [2, 3], [4, [5]]]

# print(flatten(nums))

# """
# Simple explanation:
# - isinstance(item, list) checks whether an item is a list.
# - flatten(item) handles a nested list recursively.
# - result.append(item) adds a normal element.
# - result.extend(...) adds all the elements from the flattened nested list.
# """

#QN_154
# from functools import reduce

# nums = list(map(int, input().split()))

# squares = list(map(lambda x: x ** 2, nums))
# even_numbers = list(filter(lambda x: x % 2 == 0, nums))
# total = reduce(lambda x, y: x + y, nums)

# print("map (square):", squares)
# print("filter (even):", even_numbers)
# print("reduce (sum):", total)


#QN_155
name = "Abisha"
marks = 85
text = "Python"

print(f"{name} scored {marks} marks")
print("text[1:4] →", text[1:4])
print("text[::-1] →", text[::-1])


#QN_156
try:
    a, b = map(int, input().split())
    result = a / b
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")