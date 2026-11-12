
#i represents the row number.
# j represents the column number.


#SQUARE PATTERN 
# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print("*", end=' ')
#     print()


#INCREASING TRIANGLE PATTERN
# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=' ')
#     print()


#DECREASING TRIANGLE PATTERN
# n = int(input())
# for i in range(n):
#     for j in range(i,n):
#         print("*", end=' ')
#     print()



# RIGHT SIDED UPWARD TRIANGLE
# n = int(input())
# for i in range(n):
#     for j in range(i+1, n):
#         print(" ", end=" ")
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()



#RIGHT SIDED DOWNWARD TRIANGLE
# n = int(input())
# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(i, n):
#         print("*", end=" ")
#     print()


#Hill Pattern
n = int(input())
for i in range(n):
    for j in range(i + 1, n):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()

#Reverese Hill Pattern
n = int(input())
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(i, n - 1):
        print("*", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    print()


#Diamond Pattern 
n = int(input())
# upper half
for i in range(n - 1):
    for j in range(i + 1, n):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()
# lower half
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(2 * (n - i) - 1):
        print("*", end=" ")
    print()



# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")

#     for j in range(i,n-1):
#         print("*", end=" ")

#     for j in range(i,n):
#         print("*", end=" ")

#     print()


#Number triangle (1, 12, 123)
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()


# Floyd's triangle
# n = int(input())
# num = 1

# for i in range(1, n + 1):
#     for j in range(i):
#         print(num, end=' ')
#         num += 1
#     print()


# Pascal’s Triangle
# n = int(input())
# for i in range(n):
#     num = 1
#     for j in range(i + 1):
#         print(num, end=' ')
#         num = num * (i - j) // (j + 1)
#     print()


#Hollow Square
# n = int(input())

# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# Hollow Pyramid
# n = int(input())

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")

#     for j in range(1, 2 * i):
#         if j == 1 or j == 2 * i - 1 or i == n:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()





# Alphabet patterns (A, AB, ABC)
# n = int(input())

# for i in range(n):
#     for j in range(i + 1):
#         print(chr(65 + j), end=" ")
#     print()





# Butterfly pattern
# n = int(input())

# # Upper half
# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(2 * (n - i)):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     print()

# # Lower half
# for i in range(n - 1, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(2 * (n - i)):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     print()
