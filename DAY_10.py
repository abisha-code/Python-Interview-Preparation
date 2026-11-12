#QN_95
# nums = input().split()
# numbers = []
# for num in nums:
#     numbers.append(int(num))
# print(*numbers)



#QN_96
# nums=input().split()
# numbers=[]
# for num in nums:
#     numbers.append(int(num))

# largest_element=numbers[0]
# for i in range(1,len(numbers)):
#     if numbers[i]>largest_element:
#         largest_element=numbers[i]

# max_element=max(numbers)

# print(largest_element)
# print(max_element)


#QN_97
# nums=input().split()
# numbers=[]

# for num in nums:
#     numbers.append(int(num))

# smallest_num=numbers[0]
# for i in range(0,len(numbers)):
#     if numbers[i]<smallest_num:
#         smallest_num=numbers[i]
# print(smallest_num)


#QN_98
# nums=input().split()
# numbers=[]

# for num in nums:
#     numbers.append(int(num))

# total_sum=0
# for i in range(0,len(numbers)):
#     total_sum=total_sum+numbers[i]

# print(total_sum)


#QN_99
# nums=input().split()
# numbers=[]

# for num in nums:
#     numbers.append(int(num))

# total_sum=0
# for i in range(0,len(numbers)):
#     total_sum+=numbers[i]

# total_avg=total_sum/len(numbers)

# print(total_avg)


#QN_100
# nums=input().split()
# numbers=[]

# for num in nums:
#     numbers.append(int(num))

# count=0
# for i in range(0,len(numbers)):
#     if numbers[i]%2==0:
#         count+=1

# print(count)


#QN_101
# nums=input().split()
# numbers=[]

# for num in nums:
#     numbers.append(int(num))

# count=0
# for i in range(0,len(numbers)):
#     if numbers[i]%2!=0:
#         count+=1

# print(count)


#QN_102
# nums=input().split()
# target=int(input())
# numbers=[]

# for num in nums:
#     numbers.append(int(num))

# is_found=False
# for i in range(0,len(numbers)):
#     if numbers[i]==target:
#         is_found=True

# if is_found:
#     print("Found")
# else:
#     print("Not Found")


#QN_103
# nums = list(map(int, input().split()))
# target = int(input())
# ans = -1
# for i in range(len(nums)):
#     if nums[i] == target:
#         ans = i
#         break
# print(ans)

#QN_104
# nums = input().split()
# target = int(input())
# numbers = []

# for num in nums:
#     numbers.append(int(num))

# count = 0

# for i in numbers:
#     if i == target:
#         count += 1

# print(count)


#QN_105
# nums=input().split()
# numbers=[]

# for num in nums:
#     numbers.append(int(num))

# index=int(input())
# Element=int(input())

# updated_list=[]

# for i in range(0,len(numbers)):
#     if i==index:
#         updated_list.append(Element)
#     else:
#         updated_list.append(numbers[i])

# print(updated_list)



# QN_106
# nums = list(map(int, input().split()))
# position = int(input())
# element = int(input())

# new_list = []

# for i in range(len(nums)):
#     if i == position:
#         new_list.append(element)

#     if i < len(nums):
#         new_list.append(nums[i])

# print(new_list)



#QN_107
# nums=input().split()
# numbers=[]

# for num in nums:
#     numbers.append(int(num))

# element=int(input())
# updated_list=[]
# for i in range(len(numbers)):
#     if numbers[i]==element:
#         continue
#     else:
#         updated_list.append(numbers[i])

# print(updated_list)



#QN_108
# nums=input().split()
# numbers=[]

# for num in nums:
#     numbers.append(int(num))

# first_largest=numbers[0]
# second_largest=numbers[1]

# for i in range(len(nums)):
#     if numbers[i]>first_largest:
#         second_largest=first_largest
#         first_largest=numbers[i]
        

#     elif numbers[i]<first_largest and numbers[i]>second_largest:
#         second_largest=numbers[i]

# print(second_largest)


#QN_109
# nums=input().split()
# numbers=[]

# for num in nums:
#     numbers.append(int(num))

# first_smallest=numbers[0]
# second_smallest=numbers[1]

# for i in range(len(nums)):
#     if numbers[i]<first_smallest:
#         second_smallest=first_smallest
#         first_smallest=numbers[i]
        

#     elif numbers[i]>first_smallest and numbers[i]<second_smallest:
#         second_smallest=numbers[i]

# print(second_smallest)


#QN_110
# nums = input().split()
# numbers = []

# for num in nums:
#     numbers.append(int(num))

# first_largest = float('-inf')
# second_largest = float('-inf')
# third_largest = float('-inf')

# for i in range(len(numbers)):
#     if numbers[i] > first_largest:
#         third_largest = second_largest
#         second_largest = first_largest
#         first_largest = numbers[i]

#third largest UNIQUE number
#     elif numbers[i] > second_largest and numbers[i] != first_largest:
#         third_largest = second_largest
#         second_largest = numbers[i]

#     elif numbers[i] > third_largest and numbers[i] != second_largest and numbers[i] != first_largest:
#         third_largest = numbers[i]

# print(third_largest)



#QN_111
# nums=input().split()
# numbers=[]

# for num in nums:
#     numbers.append(int(num))

# n=int(input())
# total_sum=n*(n+1)//2
# sum=0
# for i in numbers:
#     sum+=i

# missing_numbers=total_sum-sum
# print(missing_numbers)


#QN_112
# nums=input().split()
# numbers=[]

# for num in nums:
#     numbers.append(int(num))

# reversed_list=[]

# for i in range(len(numbers)-1,-1,-1):
#     reversed_list.append(numbers[i])

# print(reversed_list)


#QN_113
# nums = list(map(int, input().split()))
# k = int(input())
# print(k)
# if nums:
#     k = k % len(nums)
# new_list = []
# for i in range(k, len(nums)):
#     new_list.append(nums[i])
# for i in range(k):
#     new_list.append(nums[i])
# print(new_list)

# [1, 2, 3, 4, 5] with K = 2 gives [3, 4, 5, 1, 2].
# K = 7 behaves like K = 2.
# K = 0 or K = 5 returns the original list.


#QN_114
# nums = list(map(int, input().split()))
# k = int(input())
# if nums:
#     k = k % len(nums)
# n = len(nums)
# new_list = []
# for i in range(n - k, n):
#     new_list.append(nums[i])
# for i in range(n - k):
#     new_list.append(nums[i])
# print(new_list)



#QN_115
# nums=input().split()
# numbers=[]

# for num in nums:
#     numbers.append(int(num))

# new_list=[]
# for i in range(len(numbers)):
#     if numbers[i]!=0:
#         new_list.append(numbers[i])

# count=0
# for j in numbers:
#     if j==0:
#         count+=1

# for k in range(count):
#     new_list.append(0)

# print(new_list)



#QN_116
# nums=input().split()
# numbers=[]

# for num in nums:
#     numbers.append(int(num))

# new_list=[]

# for i in numbers:
#     if i%2==0:
#         new_list.append(i)

# for i in numbers:
#     if i%2!=0:
#         new_list.append(i)

# print(new_list)



#QN_117
# nums = list(map(int, input().split()))

# for i in range(0, len(nums)-1 , 2):
#     temp = nums[i]
#     nums[i] = nums[i + 1]
#     nums[i + 1] = temp

# print(nums)


#QN_118
# nums = list(map(int, input().split()))

# is_sorted = True

# for i in range(len(nums) - 1):
#     if nums[i] > nums[i + 1]:
#         is_sorted = False
#         break

# if is_sorted:
#     print("Sorted")
# else:
#     print("Not Sorted")



#QN_119
# nums = list(map(int, input().split()))
# seen = set()
# result = []
# for n in nums:
#     if n not in seen:
#         seen.add(n)
#         result.append(n)
# print(result)


#QN_120
# nums=input().split()
# numbers=[]
# for num in nums:
#     numbers.append(int(num))

# new_list=[]
# for i in range(len(numbers)):
#     if numbers[i] not in new_list:
#         new_list.append(numbers[i])

# print(new_list)


#QN_121
# nums = list(map(int, input().split()))
# seen = []
# dups = []
# for n in nums:
#     if n in seen and n not in dups:
#         dups.append(n)
#     if n not in seen:
#         seen.append(n)
# print(dups)



#QN_122
# nums=input().split()
# number=[]

# for num in nums:
#     number.append(int(num))

# new_dict={}
# for i in range(len(number)):
#     if number[i] not in new_dict:
#         new_dict[number[i]]=1
#     else:
#         new_dict[number[i]]+=1

# new_list=[]
# for num in new_dict:
#     if new_dict[num] == 1:
#         new_list.append(num)

# print(new_list)


#QN_123
# list1 = list(map(int, input().split()))
# list2 = list(map(int, input().split()))

# new_list = []

# for num in list1:
#     new_list.append(num)

# for num in list2:
#     new_list.append(num)

# print(new_list)


#QN_124
# nums1=input().split()
# nums2=input().split()
# number1=[]
# number2=[]

# for a in nums1:
#     number1.append(int(a))

# for b in nums2:
#     number2.append(int(b))


# new_list=[]

# for n1 in number1:
#     new_list.append(n1)

# for n2 in number2:
#     new_list.append(n2)

# for i in range(0,len(new_list)):
#     for j in range(i+1,len(new_list)):
#         if new_list[i]>new_list[j]:
#             temp=new_list[i]
#             new_list[i]=new_list[j]
#             new_list[j]=temp
# print(new_list)



#QN_125
# list1 = list(map(int, input().split()))
# list2 = list(map(int, input().split()))
# common = []
# for i in list1:
#     if i in list2 and i not in common:
#         common.append(i)



# union = list1[:]
# for i in list2:
#     if i not in union:
#         union.append(i)
# print("Common:", common)
# print("Union:", union)



#QN_126
# nums1=input().split()
# nums2=input().split()

# list1=[]
# list2=[]

# for num in nums1:
#     list1.append(int(num))

# for num in nums2:
#     list2.append(int(num))

# new_list=[]
# for i in list1:
#     if i not in list2:
#         new_list.append(i)

# print(new_list)


#QN_127
# nums = list(map(int, input().split()))
# target = int(input())
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print([i, j])
#             break
#     else:
#         print(-1)
#     break


    
#QN_128
# nums=input().split()
# number=[]

# for num in nums:
#     number.append(int(num))

# current_sum=number[0]
# max_sum=number[0]

# for i in range(1,len(number)):
#     if number[i]>number[i]+current_sum:
#         current_sum=number[i]
#     else:
#         current_sum=current_sum+number[i]

#     if current_sum>max_sum:
#         max_sum=current_sum

# print(max_sum)


#QN_129
# nums=input().split()
# number=[]

# for num in nums:
#     number.append(int(num))

# max_right = number[-1]
# leaders = [max_right]

# for i in range(len(number)-2,-1,-1):
#     if number[i] >= max_right:
#         leaders.append(number[i])
#         max_right = number[i]

# print(*leaders[::-1])


#QN_130
# nums = input().split()
# number = []

# for num in nums:
#     number.append(int(num))

# for i in range(len(number)):
#     left_sum = 0
#     right_sum = 0

#     for j in range(i):
#         left_sum += number[j]

#     for j in range(i + 1, len(number)):
#         right_sum += number[j]

#     if left_sum == right_sum:
#         print(i)
#         break
# else:
#     print(-1)


#QN_131
# nums = input().split()
# number = []

# for num in nums:
#     number.append(int(num))

# for i in range(len(number)):
#     count = 0

#     for j in range(len(number)):
#         if number[i] == number[j]:
#             count += 1

#     if count > len(number) // 2:
#         print(number[i])
#         break
# else:
#     print(-1)


#QN_132
# nums = list(map(int, input().split()))
# target = int(input())
# left, right = 0, len(nums) - 1
# while left < right:
#     s = nums[left] + nums[right]
#     if s == target:
#         print((nums[left], nums[right]))
#         break
#     elif s < target:
#         left += 1
#     else:
#         right -= 1

#QN_133
# nums = list(map(int, input().split()))
# k = int(input())

# current_sum = 0

# for i in range(k):
#     current_sum += nums[i]

# max_sum = current_sum

# for i in range(k, len(nums)):
#     current_sum = current_sum - nums[i - k] + nums[i]

#     if current_sum > max_sum:
#         max_sum = current_sum

# print(max_sum)



#QN_134
# nums = list(map(int, input().split()))

# prefix = []
# total = 0

# for num in nums:
#     total = total + num
#     prefix.append(total)

# print(prefix)





#OPTIMIZED APPROACH OTHER THAN BRUTE-FORCE APPROARCH
#QN_124
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# i = j = 0
# result = []
# while i < len(a) and j < len(b):
#     if a[i] <= b[j]:
#         result.append(a[i])
#         i += 1
#     else:
#         result.append(b[j])
#         j += 1
# while i < len(a):          # leftovers from a
#     result.append(a[i])
#     i += 1
# while j < len(b):          # leftovers from b
#     result.append(b[j])
#     j += 1
# print(result)



# #QN_127
# nums = list(map(int, input().split()))
# target = int(input())
# seen = {}                       # value -> index
# for i in range(len(nums)):
#     need = target - nums[i]
#     if need in seen:
#         print([seen[need], i])
#         break
#     seen[nums[i]] = i


# #QN_130
# nums = list(map(int, input().split()))
# total = sum(nums)
# left = 0
# for i in range(len(nums)):
#     right = total - left - nums[i]
#     if left == right:
#         print(i)
#         break
#     left += nums[i]
# else:
#     print(-1)


# #QN_131
# nums = list(map(int, input().split()))
# count = {}
# for n in nums:
#     count[n] = count.get(n, 0) + 1

# for n in count:
#     if count[n] > len(nums) // 2:
#         print(n)
#         break
# else:
#     print(-1)


# #QN 120
# nums = list(map(int, input().split()))
# seen = {}
# result = []
# for n in nums:
#     if n not in seen:
#         seen[n] = True
#         result.append(n)
# print(result)


# #QN 121
# nums = list(map(int, input().split()))
# count = {}
# for n in nums:
#     count[n] = count.get(n, 0) + 1

# dups = []
# for n in count:
#     if count[n] > 1:
#         dups.append(n)
# print(dups)


# #QN 125
# list1 = list(map(int, input().split()))
# list2 = list(map(int, input().split()))

# set2 = set(list2)
# added = set()
# common = []
# for x in list1:
#     if x in set2 and x not in added:
#         common.append(x)
#         added.add(x)

# seen = set()
# union = []
# for x in list1 + list2:
#     if x not in seen:
#         seen.add(x)
#         union.append(x)

# print("Common:", common)
# print("Union:", union)



# #QN 126
# list1 = list(map(int, input().split()))
# list2 = list(map(int, input().split()))

# set2 = set(list2)
# result = []
# for x in list1:
#     if x not in set2:
#         result.append(x)
# print(result)



# Summary of the improvement

# QN	Before	After	Technique
# 124	O(n²)	O(n)	two pointers
# 127	O(n²)	O(n)	dictionary
# 130	O(n²)	O(n)	running sum
# 131	O(n²)	O(n)	frequency dictionary
# 120, 121	O(n²)	O(n)	dictionary
# 125, 126	O(n²)	O(n)	set lookup

