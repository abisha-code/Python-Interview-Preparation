#QN_135
# A = set(map(int, input("Enter elements of A: ").split()))
# B = set(map(int, input("Enter elements of B: ").split()))

# print("Intersection:", A & B)
# print("Union:", A | B)
# print("Difference:", A - B)
# print("Symmetric difference:", A ^ B)

#QN_136
# student = {}

# student["name"] = input("Enter name: ")
# student["age"] = int(input("Enter age: "))
# student["marks"] = int(input("Enter marks: "))
# update_marks=int(input("then update marks to "))

# print("Name:",student["name"])
# print("Age:",student["age"])
# print("Marks:",student["marks"])

# student["marks"]=update_marks
# print(student)


#QN_137
# student={}

# student["name"]=input()
# student["age"]=int(input())

# for key in student:
#     print(key)


#QN_138
# student={}

# student["name"]=input()
# student["age"]=int(input())

# for key,value in student.items():
#     print(f"{value}")


#QN_139
# student={}

# student["name"]=input()
# student["age"]=int(input())

# for key,value in student.items():
#     print(f"{key}:{value}")


#QN_140
# student={}

# student["name"]=input()
# student["age"]=int(input())
# search_key=input()

# for key in student:
#     if key==search_key:
#         print("Key exists")
#         break
# else:
#     print("Key not exists")


#QN_141
# student = {"name": "Abisha"}

# key = input("Enter key: ")
# value = int(input("Enter value: "))

# student[key] = value

# print(student)

#QN_142
# student = {"name": "Abisha", "age": 22}

# key = input("Enter key to update: ")
# value = int(input("Enter new value: "))

# student[key] = value

# print(student)

#QN_143
# student = {"name": "Abisha", "age": 22}

# key = input("Enter key to delete: ")

# if key in student:
#     del student[key]

# print(student)


#QN_144
# marks={"a": 10, "b": 30, "c": 20}

# max_value=marks["a"]
# for key,value in marks.items():
#     if value>max_value:
#         max_value=value
#         print(key)


#QN_145
# A = {"a": 1, "b": 2}
# B = {"c": 3}
# C = {}

# for key, value in A.items():
#     C[key] = value

# for key, value in B.items():
#     C[key] = value

# print(C)


#QN_146
# student = {"a": 3, "b": 1, "c": 2}

# items = list(student.items())
# print(items)
# for i in range(len(items)):
#     for j in range(i + 1, len(items)):
#         if items[i][1] > items[j][1]:
#             items[i], items[j] = items[j], items[i]

# sorted_dict = dict(items)

# print(sorted_dict)


#QN_147
# nums=list(map(int,input().split()))

# new_list={}
# for i in nums:
#     if i not in new_list:
#         new_list[i]=1
#     else:
#         new_list[i]+=1

# print(new_list)

#QN_148
# word = input()

# new_dict = {}

# for i in word:
#     if i not in new_dict:
#         new_dict[i] = 1
#     else:
#         new_dict[i] += 1

# for key, value in new_dict.items():
#     print(key, ":", value)

#QN_149
# word = input().split()
# print(word)
# new_dict = {}

# for i in word:
#     if i not in new_dict:
#         new_dict[i] = 1
#     else:
#         new_dict[i] += 1

# for key, value in new_dict.items():
#     print(key, ":", value)


#QN_150
# nums = list(map(int, input().split()))

# frequency = {}

# for num in nums:
#     if num not in frequency:
#         frequency[num] = 1
#     else:
#         frequency[num] += 1

# for key, value in frequency.items():
#     print(key, ":", value)