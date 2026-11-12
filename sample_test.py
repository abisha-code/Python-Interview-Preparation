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
# reversed_str=""
# for i in range(len(text)-1,-1,-1):
#     reversed_str+=text[i]
# print(reversed_str)



#QN_64
# text=input()
# reversed_str=""
# for i in range(len(text)-1,-1,-1):
#     reversed_str+=text[i]

# if reversed_str==text:
#     print("palidrome")
# else:
#     print("Not palindrome")



#QN_65
# text=input()
# result=""
# for c in text:
#     if c!=" ":
#         result+=c
# print(result)


#QN_66
# text=input()
# result=""
# for c in text:
#     if 65<=ord(c)<=90:
#         result+=chr(ord(c)+32)
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
#     if c==" ":
#         new_word=True
#         result+=c

#     elif new_word:
#         if 97<=ord(c)<=122:
#             result+=chr(ord(c)-32)
#         else:
#             result+=c
#         new_word=False
#     else:
#         result+=c

# print(result)


#QN_69
# text=input()
# result=""
# for c in text:
#     if c.lower() not in "aieou":
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
# text=input()
# vowel_count=0
# const_count=0
# vowel_list=""
# const_list=""
# for c in text:
#     if c.lower() in "aeiou":
#         vowel_count+=1
#         vowel_list+=c
#     else:
#         const_count+=1
#         const_list+=c

# print(f"Vowels:{vowel_count} ({",".join(vowel_list)})")
# print(f"Consonants: {const_count} ({",".join(const_list)})")



#QN_72
# text=input()
# target=input()
# count=0
# for c in text:
#     if c==target:
#         count+=1
# print(count)


#QN_73
# text=input()
# isdigit=0
# isalpha=0
# isspl=0
# for c in text:
#     if c.isdigit():
#         isdigit+=1
#     elif c.isalpha():
#         isalpha+=1
#     else:
#         isspl+=1

# print(f"Letters: {isdigit}")
# print(f"Digits: {isalpha}")
# print(f"Special characters: {isspl}")


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
#         if text[i]==text[j]:
#             count+=1

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

# max_count=0
# max_char=""

# for char in freq_char:
#     if freq_char[char]>max_count:
#         max_count=freq_char[char]
#         max_char=char

# print(f"{max_char} ({max_count} times)")


# #QN_79
# text=input()
# freq_char={}

# for c in text:
#     if c in freq_char:
#         freq_char[c]+=1
#     else:
#         freq_char[c]=1

# while len(freq_char)>0:
#     max_count=0
#     max_char=""
#     for char in freq_char:
#         if freq_char[char]>max_count:
#             max_count=freq_char[char]
#             max_char=char
#     print(f"{max_char}:{max_count}")
#     del freq_char[char]



#QN_80
# str1=input()
# str2=input()

# if len(str1)!=len(str2):
#     print("Not Anagram")
# else:
#     freq_char1={}
#     freq_char2={}
#     for c in str1:
#         if c in freq_char1:
#             freq_char1[c]+=1
#         else:
#             freq_char1[c]=1

#     for c in str2:
#         if c in freq_char2:
#             freq_char2[c]+=1
#         else:
#             freq_char2[c]=1

#     if freq_char1==freq_char2:
#         print("Anagram")
#     else:
#         print("Not Anagram")



#QN_81
# str1=input()
# str2=input()

# if len(str1)==len(str2) and str2 in str1+str1:
#     print("Rotation")
# else:
#     print("Not Rotation")





#---------------------------ARRAYS----------------------------\
#QN_112
# nums=list(map(int,input().split()))
# reversed_list=[]

# for i in range(len(nums)-1,-1,-1):
#     reversed_list.append(nums[i])

# print(*reversed_list)


#QN_113
# nums=list(map(int,input().split()))
# k=int(input())
# if nums:
#     k=k%len(nums)

# roated_list=[]
# for i in range(k,len(nums)):
#     roated_list.append(nums[i])

# for j in range(k):
#     roated_list.append(nums[j])

# print(*roated_list)


#QN_114
# nums=list(map(int,input().split()))
# k=int(input())
# if nums:
#     k=k%len(nums)

# roated_list=[]
# n=len(nums)
# for i in range(n-k,n):
#     roated_list.append(nums[i])

# for j in range(n-k):
#     roated_list.append(nums[j])

# print(*roated_list)


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

# for i in range(0,len(nums)-1,2):
#     temp=nums[i]
#     nums[i]=nums[i+1]
#     nums[i+1]=temp

# print(nums)


#QN_118
# nums=list(map(int,input().split()))

# sorted=True
# for i in range(0,len(nums)-1):
#     if nums[i]>nums[i+1]:
#         sorted=False

# if sorted:
#     print("sorted")

# else:
#     print("not sorted")



#QN_119
# nums=list(map(int,input().split()))

# result=[]

# for num in nums:
#     if num not in result:
#         result.append(num)

# print(result)


#QN_120
# nums=list(map(int,input().split()))


# result=[]
# dup=[]

# for num in nums:
#     if num in result and num not in dup:
#         dup.append(num)
#     else:
#         result.append(num)

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
# for num in freq_char:
#     if freq_char[num]==1:
#         result.append(num)


# print(result)



#QN_127
# nums=list(map(int,input().split()))
# target=int(input())

# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j]==target:
#             print(i,j)
#             break
#     else:
#         print(-1)
#     break



#QN_128
# nums=list(map(int,input().split()))

# max_sum=nums[-1]
# current_sum=max_sum

# for num in nums:
#     if num>current_sum:
#         current_sum=num
#     else:
#         current_sum=current_sum+num

#     if current_sum>max_sum:
#         max_sum=current_sum

# print(max_sum)



#QN_129
# nums=list(map(int,input().split()))
# max_right=nums[-1]
# leaders=[max_right]

# for i in range(len(nums)-2,-1,-1):
#     if nums[i]>=max_right:
#         leaders.append(nums[i])
#         max_right=nums[i]

# print(*leaders[::-1])


#QN_130
# nums=list(map(int,input().split()))
# for i in range(len(nums)):
#     left_sum=0
#     right_sum=0
#     for j in range(i):
#         left_sum+=nums[i]
#     for j in range(i+1,len(nums)):
#         right_sum+=nums[i]

#     if left_sum==right_sum:
#         print(i)
#         break
# else:
#     print(-1)



#QN_131
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



#QN_132
# nums=list(map(int,input().split()))
# target=int(input())
# left=0
# right=len(nums)-1

# while left<right:
#     s=nums[left]+nums[right]
#     if s==target:
#         print(nums[left],nums[right])
#         break
#     elif s<target:
#         left+=1
#     else:
#         right-=1



#QN_134

# nums=list(map(int,input().split()))
# sum=0
# result=[]
# for num in nums:
#     sum+=num
#     result.append(sum)

# print(result)



#QN_133
# nums=list(map(int,input().split()))
# k=int(input())

# current_sum=0
# for i in range(k):
#     current_sum+=nums[i]

# max_sum=current_sum

# for i in range(k,len(nums)):
#     current_sum=current_sum-nums[i-k]+nums[i]

#     if current_sum>max_sum:
#         max_sum=current_sum

# print(max_sum)
