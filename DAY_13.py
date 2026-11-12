#QN_157
# nums=list(map(int,input().split()))
# target=int(input())

# low=0 
# high=len(nums)-1

# while low<=high:
#     mid=(low+high)//2
#     if nums[mid]==target:
#         print(f"Found at index {mid}")
#         break
#     elif nums[mid]<target:
#         low=mid+1
#     else:
#         high=mid-1



#QN_158
# nums = list(map(int, input().split()))
# target = int(input())

# low = 0
# high = len(nums)

# while low < high:
#     mid = (low + high) // 2

#     if nums[mid] < target:
#         low = mid + 1
#     else:
#         high = mid

# print(low)


#QN_159
# nums = list(map(int, input().split()))
# target = int(input())

# low = 0
# high = len(nums) - 1
# result = -1

# while low <= high:
#     mid = (low + high) // 2
#     if nums[mid]==target:
#         result=mid
#         high=mid-1
#     elif nums[mid] < target:
#         low = mid + 1
#     else:
#         high = mid-1
# print(result)


#QN_160
# nums = list(map(int, input().split()))
# target = int(input())

# low = 0
# high = len(nums) - 1
# result = -1

# while low <= high:
#     mid = (low + high) // 2
#     if nums[mid]==target:
#         result=mid
#         low=mid+1
#     elif nums[mid] < target:
#         low = mid + 1
#     else:
#         high = mid-1

# print(result)


#QN_161

# nums = list(map(int, input().split()))
# target = int(input())

# low = 0
# high = len(nums) - 1
# first = -1

# # Find the first occurrence
# while low <= high:
#     mid = (low + high) // 2

#     if nums[mid] == target:
#         first = mid
#         high = mid - 1
#     elif nums[mid] < target:
#         low = mid + 1
#     else:
#         high = mid - 1

# low = 0
# high = len(nums) - 1
# last = -1

# # Find the last occurrence
# while low <= high:
#     mid = (low + high) // 2

#     if nums[mid] == target:
#         last = mid
#         low = mid + 1
#     elif nums[mid] < target:
#         low = mid + 1
#     else:
#         high = mid - 1

# if first == -1:
#     print(0)
# else:
#     print(last - first + 1)


#QN_162

# nums = list(map(int, input().split()))
# target = int(input())

# low = 0
# high = len(nums) - 1

# result = -1

# while low <= high:
#     mid = (low + high) // 2

#     if nums[mid] <= target:
#         result = nums[mid]
#         low = mid + 1
#     else:
#         high = mid - 1

# print(result)


#QN_163

# nums = list(map(int, input().split()))
# target = int(input())

# low = 0
# high = len(nums) - 1
# result = -1

# while low <= high:
#     mid = (low + high) // 2

#     if nums[mid] >= target:
#         result = nums[mid]
#         high = mid - 1
#     else:
#         low = mid + 1

# print(result)


#QN 164
# n = int(input())

# low = 0
# high = n
# result = 0

# while low <= high:
#     mid = (low + high) // 2

#     if mid * mid <= n:
#         result = mid
#         low = mid + 1
#     else:
#         high = mid - 1

# print(result)


#QN_165

nums = list(map(int, input().split()))

low = 0
high = len(nums) - 1

while low < high:
    mid = (low + high) // 2

    if nums[mid] < nums[mid + 1]:
        low = mid + 1
    else:
        high = mid

print(low)


#QN_166

nums = list(map(int, input().split()))
target = int(input())

low = 0
high = len(nums) - 1
result = -1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
        result = mid
        break

    # Check whether the left half is sorted
    if nums[low] <= nums[mid]:
        if nums[low] <= target and target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1

    # Otherwise, the right half is sorted
    else:
        if nums[mid] < target and target <= nums[high]:
            low = mid + 1
        else:
            high = mid - 1

print(result)

