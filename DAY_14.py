
#QN_167
# nums = list(map(int, input().split()))

# for i in range(len(nums) - 1):
#     for j in range(len(nums) - 1):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]

# print(nums)


#QN_168
# numbers = [5, 3, 4, 1]

# for i in range(len(numbers)):
#     min_index = i

#     for j in range(i + 1, len(numbers)):
#         if numbers[j] < numbers[min_index]:
#             min_index = j

#     numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

# print(numbers)


#QN_169
# numbers = [5, 3, 4, 1]
# for i in range(1, len(numbers)):
#     key = numbers[i]
#     j = i - 1
#     while j >= 0 and numbers[j] > key:
#         numbers[j + 1] = numbers[j]
#         j -= 1
#     numbers[j + 1] = key
# print(numbers)

#QN_170

# numbers = [5, 3, 4, 1]

# def merge_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers

#     mid = len(numbers) // 2

#     left = merge_sort(numbers[:mid])
#     right = merge_sort(numbers[mid:])

#     result = []
#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result

# print(merge_sort(numbers))



#QN_171

# numbers = [5, 3, 4, 1]

# def quick_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers

#     pivot = numbers[-1]
#     left = []
#     right = []

#     for num in numbers[:-1]:# :-1 returns the last before elements
#         if num <= pivot:
#             left.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + [pivot] + quick_sort(right)

# print(quick_sort(numbers))



# #QN_172
# numbers = [3,1,2]

# def quick_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers

#     pivot = numbers[-1]
#     left = []
#     right = []

#     for num in numbers[:-1]:# :-1 returns the last before elements
#         if num <= pivot:
#             left.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + [pivot] + quick_sort(right)

# print(quick_sort(numbers))


#QN_173
# strings = ["banana", "apple", "cherry"]

# def quick_sort(strings):
#     if len(strings) <= 1:
#         return strings

#     pivot = strings[-1]
#     left = []
#     right = []

#     for word in strings[:-1]:
#         if word <= pivot:
#             left.append(word)
#         else:
#             right.append(word)

#     return quick_sort(left) + [pivot] + quick_sort(right)

# print(quick_sort(strings))


#QN_174
# numbers = [4, 5, 6, 5, 4, 4]

# frequency = {}

# # Count frequency
# for num in numbers:
#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1

# def quick_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers

#     pivot = numbers[-1]
#     left = []
#     right = []

#     for num in numbers[:-1]:
#         if frequency[num] >= frequency[pivot]:
#             left.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + [pivot] + quick_sort(right)

# print(quick_sort(numbers))


#QN_175

# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

# # Sort intervals by starting value using Merge Sort
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i][0] <= right[j][0]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result

# intervals = merge_sort(intervals)

# merged = []

# for interval in intervals:
#     if not merged or interval[0] > merged[-1][1]:
#         merged.append(interval)
#     else:
#         merged[-1][1] = max(merged[-1][1], interval[1])

# print(merged)


#QN_176
# arr = list(map(int, input().split()))

# count = 0

# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] > arr[j]:
#             count += 1

# print(count)


#QN_177

# numbers = [2, 0, 2, 1, 1, 0]

# def quick_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers

#     pivot = numbers[-1]
#     left = []
#     right = []

#     for num in numbers[:-1]:
#         if num <= pivot:
#             left.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + [pivot] + quick_sort(right)

# print(quick_sort(numbers))


#QN_178

# numbers = [3, 2, 1, 5, 6, 4]
# k = 2

# def quick_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers

#     pivot = numbers[-1]
#     left = []
#     right = []

#     for num in numbers[:-1]:
#         if num <= pivot:
#             left.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + [pivot] + quick_sort(right)


# sorted_numbers = quick_sort(numbers)

# print(sorted_numbers[-k])


#QN_179
# numbers = [1, 1, 1, 2, 2, 3]
# k = 2

# frequency = {}

# # Count frequency
# for num in numbers:
#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1


# def quick_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers

#     pivot = numbers[-1]
#     left = []
#     right = []

#     for num in numbers[:-1]:
#         if frequency[num] >= frequency[pivot]:
#             left.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + [pivot] + quick_sort(right)


# unique_numbers = list(frequency.keys())

# sorted_numbers = quick_sort(unique_numbers)

# print(sorted_numbers[:k])


#QN_180

# words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# def quick_sort(chars):
#     if len(chars) <= 1:
#         return chars

#     pivot = chars[-1]
#     left = []
#     right = []

#     for ch in chars[:-1]:
#         if ch <= pivot:
#             left.append(ch)
#         else:
#             right.append(ch)

#     return quick_sort(left) + [pivot] + quick_sort(right)


# groups = {}

# for word in words:
#     sorted_chars = quick_sort(list(word))
#     key = "".join(sorted_chars)

#     if key in groups:
#         groups[key].append(word)
#     else:
#         groups[key] = [word]

# result = list(groups.values())

# print(result)



#QN_181

# meetings = [[0, 30], [5, 10], [15, 20]]

# def quick_sort(meetings):
#     if len(meetings) <= 1:
#         return meetings

#     pivot = meetings[-1]
#     left = []
#     right = []

#     for meeting in meetings[:-1]:
#         if meeting[0] <= pivot[0]:
# #meeting[0] → Current meeting's starting time.
# #pivot[0] → Pivot meeting's starting time.
#             left.append(meeting)
#         else:
#             right.append(meeting)

#     return quick_sort(left) + [pivot] + quick_sort(right)


# sorted_meetings = quick_sort(meetings)

# result = True

# for i in range(len(sorted_meetings) - 1):
#     if sorted_meetings[i][1] > sorted_meetings[i + 1][0]:
#         result = False
#         break


#Current ending time > Next starting time → Overlap.
# Current ending time <= Next starting time → No overlap.

# print(result)



#QN_182

numbers = [7, 10, 4, 3, 20, 15]
k = 3

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[-1]
    left = []
    right = []

    for num in numbers[:-1]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    return quick_sort(left) + [pivot] + quick_sort(right)


sorted_numbers = quick_sort(numbers)

print(sorted_numbers[k - 1])





