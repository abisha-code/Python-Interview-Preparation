#QN_31
# num=int(input())
# if num<=1:
#     print("Not a Prime Number")

# else:
#     for i in range(2,num):
#         if num%i==0:
#             print("Not a Prime Number")
#             break
#     else:
#         print("Prime Number")


#QN_32
# a,b=map(int,input().split())
# prime_list=[]
# for num in range(a,b+1):
#     for i in range(2,num):
#         if num%i==0:
#             continue
#         else:
#             prime_list.append(i)
# print(prime_list)


#QN_33
# num=int(input())
# prime_list=[]
# number=2
# while len(prime_list)<num:
#     is_prime=True
#     for i in range(2,number):
#         if number%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         prime_list.append(number)
#     number+=1

# print(prime_list)


#QN_34
# num=int(input())
# factor=num
# prime_list=[]
# while factor>1:
#     for i in range(2,factor):
#         if factor%i==0:
#             prime_list.append(i)
#             factor//=i
#         else:
#             factor+=1
# print(prime_list)


#QN_35
# a,b=map(int,input().split())
# while b!=0:
#     rem=b%a
#     a=b
#     b=rem

# print(a)


#QN_36
# a,b=map(int,input().split())
# x=a
# y=b

# while y!=0:
#     rem=y%x
#     x=y
#     y=rem

# gcd=x
# lcm=(a*b)//gcd
# print(lcm)


#QN_37
# a,b=map(int,input().split())
# power=1
# for i in range(abs(5)):
#     power=power*a
# if b<0:
#     power=1/power
# print(power)

#QN_38
# num=int(input())
# if num<=1:
#     print("Not a power of 2")
# else:
#     while num%2==0:
#         num//=2
#     if num==1:
#         print("Power of 2")
#     else:
#         print("Not a Power of 2")


#QN_39
# num=int(input())
# binary=""

# if num==0:
#     print("0")

# while num>0:
#     rem=num%2
#     binary=str(rem)+binary
#     num//=2

# print(binary)

#QN_40
# binary=input()
# decimal=0
# for i in binary:
#     decimal=decimal*2+int(i)

# print(decimal)

#QN_41
# num=int(input())
# octal=""

# if num==0:
#     print("0")

# while num>0:
#     rem=num%8
#     octal=str(rem)+octal
#     num//=8

# print(octal)


#QN_42
# num=int(input())
# hexadecimal=""
# chars="0123456789ABCDEF"


# if num==0:
#     print("0")

# while num>0:
#     rem=num%16
#     hexadecimal=chars[rem]+hexadecimal
#     num//=16

# print(hexadecimal)

#QN_42
# num=int(input())
# count=0

# while num>0:
#     rem=num%2
#     count+=rem
#     num//=2

# print(count)

#QN_53
# def square(num):
#     return num*num

# n=int(input())
# print(square(n))


#QN_54
# def largest(num):
#     largest_num=num[0]
#     for i in num:
#         if i>largest_num:
#             largest_num=i
#     return largest_num

# n=list(map(int,input().split()))
# print(largest(n))


#QN_55
# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact*=i
#     return fact

# print(factorial(int(input())))



#PART=12
#QN_151
# nums=list(map(int,input().split()))

# square=[num**2 for num in nums]
# even_num=[num for num in nums if num%2==0]

# print(square)
# print(even_num)

#QN_152
# nums=list(map(int,input().split()))
# if nums==nums[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


#QN_153
# def flatten(nums):
#     result=[]
#     for item in nums:
#         if isinstance(item,list):
#             result.extend(flatten(item))
#         else:
#             result.append(item)
#     return result

# nums=[1, [2, 3], [4, [5]]]
# print(flatten(nums))

#QN_154
# from functools import reduce
# nums=list(map(int,input().split()))

# square=list(map(lambda x:x**2,nums))
# even=list(filter(lambda x:x%2==0,nums))
# sum=reduce(lambda x,y:x+y,nums)

# print(square)
# print(even)
# print(sum)


#QN_155
# name = "Abisha"
# marks = 85
# text = "Python"

# print(f"{name} scored {marks} marks")
# print(text[1:4])
# print(text[::-1])

#QN_156
# try:
#     a,b=map(int,input().split())
#     result=a//b
#     print(result)

# except ZeroDivisionError:
#     print("Cannot divide by zero")



#PART-9

#QN_61
# text=input()
# for c in text:
#     print(c)


#QN_62
# text=input()
# count=0
# for c in text:
#     count+=1
# print(count)

#QN_63
# text=input()
# length=len(text)-1
# reversed_string=""
# for c in range(length,-1,-1):
#     reversed_string+=text[c]

# print(reversed_string)



#QN_65
# str1=input()
# str2=""
# for c in range(len(str1)-1,-1,-1):
#     str2+=str1[c]

# if str1==str2:
#     print("Palindrome")

# else:
#     print("Not Palindrome")


#QN_66
# text=input()
# result=""
# for c in text:
#     if 65<=ord(c)<=90:
#         # print(ord(c))
#         lowercase=chr((ord(c))+32)
#         result+=lowercase
#     else:
#         result+=c
# print(result)


#QN_67
# text=input()
# result=""
# for c in text:
#     if 65<=ord(c)<=90:
#         result+=chr(ord(c)+32)
#     elif 97<=ord(c)<=122:
#         result+=chr(ord(c)-32)
#     else:
#         result+=c

# print(result)


#QN_68
# text=input()
# new_word=True
# result=""
# for c in text:
#     if new_word and 97<=ord(c)<=122:
#         result+=chr(ord(c)-32)
#         new_word=False
#     else:
#         result+=c
#     if c==" ":
#         new_word=True

# print(result)


#QN_69
# text=input().lower()
# result=""
# for c in text:
#     if c not in "aeiou":
#         result+=c
    
# print(result)


#QN_70
# text=input()
# count=1
# for c in text:
#     if c==" ":
#         count+=1

# print(count)

#QN_71
# text=input().lower()
# vowels_count=0
# constonants_Count=0

# for c in text:
#     if c in "aeiou":
#         vowels_count+=1
#     else:
#         constonants_Count+=1

# print(vowels_count)
# print(constonants_Count)


#QN_72
# text=input()
# char=input()
# count=0
# for c in text:
#     if c==char:
#         count+=1
# print(count)



#QN_73
# text=input()
# letter_count=0
# digits_count=0
# special_char=0
# for c in text:
#     if c.isalpha():
#         letter_count+=1
#     elif c.isdigit():
#         digits_count+=1
#     else:
#         special_char+=1

# print(letter_count)
# print(digits_count)
# print(special_char)



#QN_74
# text=input()
# dupl_char=""
# for i in range(len(text)):
#     for j in range(i+1,len(text)):
#         if text[i]==text[j] and text[i] not in dupl_char:
#             dupl_char+=text[i]

# print(dupl_char)


#QN_75

# text=input()
# result=""

# for c in text:
#     if c not in result:
#         result+=c
# print(result)


#QN_76
# text=input()

# for i in range(len(text)):
#     count=0
#     for j in range(len(text)):
#         if text[i]==text[j]:
#             count+=1
#     if count==1:
#         print(text[i])
#         break

#QN_77
# text=input()

# for i in range(len(text)):
#     count=0
#     for j in range(len(text)):
#         count+=1

#     if count>1:
#         print(text[i])
#         break


#QN_78
# text=input()
# freq_char={}

# for c in text:
#     if c in freq_char:
#         freq_char[c]+=1
#     else:
#         freq_char[c]=1

# max_char=""
# max_count=0

# for c in freq_char:
#     if freq_char[c]>max_count:
#         max_count=freq_char[c]
#         max_char=c

# print(max_char)


#QN_79
# text=input()
# freq_char={}

# for c in text:
#     if c in freq_char:
#         freq_char[c]+=1
#     else:
#         freq_char[c]=1

# print(freq_char)

#QN_80
# str1=input()
# str2=input()

# if len(str1)!=len(str2):
#     print("Not Anagram")

# else:
#     freq_char1={}
#     freq_char2={}

#     for char in freq_char1:
#         if char in freq_char1:
#             freq_char1[char]+=1
#         else:
#             freq_char1+=1

#     for char in freq_char2:
#         if char in freq_char2:
#             freq_char2[char]+=1
#         else:
#             freq_char2+=1

# if freq_char1==freq_char2:
#     print("Anagram")
# else:
#     print("Not Anagram")


#QN_81
# str1=input()
# str2=input()

# if len(str1)==len(str2) and str2 in str1+str1:
#     print("Rotation")
# else:
#     print("Not Rotation")


#QN_82
# words = input().split()
# freq_char = {}

# for word in words:
#     count = 0
#     for c in word:
#         count += 1

#     freq_char[word] = count

# max_word = ""
# max_count = 0

# for char in freq_char:
#     if freq_char[char] > max_count:
#         max_count = freq_char[char]
#         max_word = char

# print(max_word)
        

# #QN_83
# words=input().split()
# freq_char={}

# for word in words:
#     count=0
#     for c in word:
#         count+=1

#     freq_char[word]=count

# min_word=""
# min_count=float('inf')

# for word in freq_char:
#     if freq_char[word]<min_count:
#         min_count=freq_char[word]
#         min_word=word

# print(min_word)


#QN_84
# words=input().split()
# reversed_list=[]
# for word in words:
#     rev=""
#     for c in word:
#         rev=c+rev
#     reversed_list.append(rev)

# print(" ".join(reversed_list))


#QN_85
# words=input().split()
# reversed_list=[]
# for word in range(len(words)-1,-1,-1):
#     reversed_list.append(words[word])

# print(" ".join(reversed_list))



#PART-10

#QN_95
# nums=input().split()
# numbers=[]

# for num in nums:
#     numbers.append(int(num))

# print(*numbers)


#QN_96
# nums=list(map(int,input().split()))
# largest_element=nums[0]

# for i in nums:
#     if i>largest_element:
#         largest_element=i

# print(largest_element)


#QN_97
# nums=list(map(int,input().split()))

# smallest_element=nums[0]

# for num in nums:
#     if num<smallest_element:
#         smallest_element=num

# print(smallest_element)


#QN_98
# nums=list(map(int,input().split()))

# sum=0
# for num in nums:
#     sum+=num

# print(sum)


#QN_99
# nums=list(map(int,input().split()))

# sum=0
# for num in nums:
#     sum+=num

# avg=sum//len(nums)
# print(avg)

#QN_100
# nums=list(map(int,input().split()))

# count=0
# for num in nums:
#     if num%2==0:
#         count+=1

# print(count)

#QN_101
# nums=list(map(int,input().split()))

# count=0
# for num in nums:
#     if num%2!=0:
#         count+=1

# print(count)

#QN_102
# nums=list(map(int,input().split()))

# target=int(input())

# for num in nums:
#     if num==target:
#         print("Found")
#         break
# else:
#     print("Not found")


#QN_103
# nums=list(map(int,input().split()))
# target=int(input())
# for i in range(0,len(nums)):
#     if nums[i]==target:
#         print(i)


#QN_104
# nums=list(map(int,input().split()))
# target=int(input())

# count=0
# for num in nums:
#     if num==target:
#         count+=1

# print(count)


#QN_105
# nums=list(map(int,input().split()))

# index=int(input())
# element=int(input())

# result=[]
# for i in range(0,len(nums)):
#     if i==index:
#         result.append(element)
#     else:
#         result.append(nums[i])

# print(result)


#QN_106
# nums=list(map(int,input().split()))
# index=int(input())
# element=int(input())
# result=[]
# for i in range(0,len(nums)):
#     if i==index:
#         result.append(element)

#     if i<len(nums):
#         result.append(nums[i])

# print(result)


#QN_107
# nums=list(map(int,input().split()))

# element=int(input())

# result=[]
# for num in nums:
#     if num!=element:
#         result.append(num)

# print(result)


#QN_108
# nums=list(map(int,input().split()))
# first_largest=nums[0]
# second_largest=nums[1]

# for num in nums:
#     if num>first_largest:
#         second_largest=first_largest
#         first_largest=num

# print(second_largest)

#QN_109
# nums=list(map(int,input().split()))
# first_largest=nums[0]
# second_largest=nums[1]

# for num in nums:
#     if num<first_largest:
#         second_largest=first_largest
#         first_largest=num

# print(second_largest)

#QN_110
# nums=list(map(int,input().split()))

# first_largest=nums[0]
# second_largest=nums[1]
# third_largest=nums[2]

# for num in nums:
#     if num>first_largest:
#         third_largest=second_largest
#         second_largest=first_largest
#         first_largest=num

#     elif num>second_largest and num!=first_largest:
#         third_largest=second_largest
#         second_largest=num

#     elif num>third_largest and num!=first_largest and num!=second_largest:
#         third_largest=num

# print(third_largest)

    
#QN_111
# nums=list(map(int,input().split()))
# n=int(input())

# sum=0
# total_sum=n*(n+1)/2
# for num in nums:
#     sum+=num

# missing_num=int(total_sum-sum)

# print(missing_num)



#QN_112
# nums=list(map(int,input().split()))

# reversed_list=[]

# for num in range(len(nums)-1,-1,-1):
#     reversed_list.append(nums[num])

# print(reversed_list)


#QN_113
# nums=list(map(int,input().split()))
# k=int(input())
# if nums:
#     k=k%len(nums)

# result=[]
# for i in range(k,len(nums)):
#     result.append(nums[i])

# for j in range(k):
#     result.append(nums[j])

# print(result)


#QN_114
# nums=list(map(int,input().split()))
# k=int(input())
# if nums:
#     k=k%len(nums)

# n=len(nums)
# result=[]
# for i in range(n-k,n):
#     result.append(nums[i])

# for j in range(n-k):
#     result.append(nums[j])

# print(result)


#QN_115
# nums=list(map(int,input().split()))

# result=[]

# for num in nums:
#     if num!=0:
#         result.append(num)

# count=0
# for num in nums:
#     if num==0:
#         count+=1

# for i in range(count):
#     result.append(0)

# print(result)

#QN_116
# nums=list(map(int,input().split()))

# result=[]

# for num in nums:
#     if num%2==0:
#         result.append(num)

# for num in nums:
#     if num%2!=0:
#         result.append(num)

# print(result)

#QN_117
# nums=list(map(int,input().split()))


# for i in range(0,len(nums)-1,2):
#     temp=nums[i]
#     nums[i]=nums[i+1]
#     nums[i+1]=temp

# print(nums)

#QN_118
# nums=list(map(int,input().split()))

# is_sorted=True
# for i in range(len(nums)-1):
#     if nums[i]>nums[i+1]:
#         is_sorted=False
#         break

# if is_sorted:
#     print("sorted")

# else:
#     print("not sorted")



#QN_119
# nums=list(map(int,input().split()))

# seen=set()
# dup=[]

# for num in nums:
#     if num not in seen:
#         seen.add(num)
#     else:
#         dup.append(num)

# print(seen)


#QN_120
# nums=list(map(int,input().split()))

# dup=[]

# for num in nums:
#     if num not in dup:
#         dup.append(num)

# print(dup)

#QN_121
# nums=list(map(int,input().split()))
# dup=[]
# seen=[]

# for num in nums:
#     if num in seen and num not in dup:
#         dup.append(num)

#     if num not in seen:
#         seen.append(num)

# print(dup) 


#QN_122
# nums=list(map(int,input().split()))
# freq_char={}
# for num in nums:
#     if num in freq_char:
#         freq_char[num]+=1
#     else:
#         freq_char[num]=1
# result=[]
# for i in freq_char:
#     if freq_char[i]==1:
#         result.append(i)
# print(result)



#QN_123
# nums1=list(map(int,input().split()))
# nums2=list(map(int,input().split()))

# result=[]

# for i in nums1:
#     result.append(i)
# for j in nums2:
#     result.append(j)

# print(result)

#QN_124
# nums1=list(map(int,input().split()))
# nums2=list(map(int,input().split()))

# result=[]

# for i in nums1:
#     result.append(i)
# for j in nums2:
#     result.append(j)
# for i in range(0,len(result)-1):
#     if result[i]>result[i+1]:
#         temp=result[i]
#         result[i]=result[i+1]
#         result[i+1]=temp

# print(result)


#QN_125
# nums1=list(map(int,input().split()))
# nums2=list(map(int,input().split()))


# common_list=[]
# for num in nums1:
#     if num in nums2:
#         common_list.append(num)

# union_list=nums1[:]
# for num in nums2:
#     if num not in union_list:
#         union_list.append(num)

# print(union_list)
# print(common_list)



#QN_126
# nums1=list(map(int,input().split()))
# nums2=list(map(int,input().split()))
# result=[]
# for num in nums1:
#     if num not in nums2:
#         result.append(num)

# print(result)


#QN_27
# nums1=list(map(int,input().split()))
# target=int(input())

# for i in range(0,len(nums1)):
#     for j in range(i+1,len(nums1)):
#         if nums1[i]+nums1[j]==target:
#             print(i,j)
#             break

# else:
#     print(-1)
    

#QN_28
# nums1=list(map(int,input().split()))

# max_sum=nums1[0]
# current_sum=nums1[0]

# for i in range(1,len(nums1)):
#     if nums1[i]>nums1[i]+current_sum:
#         current_sum=nums1[i]
#     else:
#         current_sum=nums1[i]+current_sum

#     if current_sum>max_sum:
#         max_sum=current_sum

# print(max_sum)


#QN_29
# nums=list(map(int,input().split()))

# max_right=nums[-1]
# leader=[max_right]
# for i in range(len(nums)-2,-1,-1):
#     if nums[i]>max_right:
#         max_right=nums[i]
#         leader.append(nums[i])

# print(leader[::-1])

#QN_30
# nums=list(map(int,input().split()))

# for i in range(len(nums)):
#     left_Sum=0
#     right_sum=0

#     for j in range(i):
#         left_Sum+=nums[i]

#     for k in range(i+1,len(nums)):
#         right_sum+=nums[i]

#     if left_Sum==right_sum:
#         print(i)
#         break
# else:
#     print(-1)

#QN_31
# nums=list(map(int,input().split()))

# for i in range(len(nums)):
#     count=0
#     for j in range(len(nums)):
#         if nums[i]==nums[j]:
#             count+=1

#     if count>len(nums)//2:
#         print(nums[i])
#         break
# else:
#     print(-1)
    
