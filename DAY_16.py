#QN_198

# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))

# matrix = []

# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)


# for i in range(rows):
#     for j in range(cols):
#         print(matrix[i][j], end=" ")
#     print()


#QN_199

# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))

# matrix = []
# total = 0

# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# for i in range(rows):
#     for j in range(cols):
#         total += matrix[i][j]

# print(total)


#QN_200
# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))

# matrix = []

# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# # Find the sum of each row
# print("Row sums:", end=" ")

# for i in range(rows):
#     total = 0

#     for j in range(cols):
#         total += matrix[i][j]

#     print(total, end=" ")

# print()

# # Find the sum of each column
# print("Column sums:", end=" ")

# for j in range(cols):
#     total = 0

#     for i in range(rows):
#         total += matrix[i][j]

#     print(total, end=" ")


#QN_201
# rows = int(input())
# cols = int(input())

# matrix = []

# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# for j in range(cols):
#     for i in range(rows):
#         print(matrix[i][j], end=" ")
#     print()


#QN_202
# rows = 2
# cols = 2

# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]

# add = []
# subtract = []

# for i in range(rows):
#     add_row = []
#     sub_row = []

#     for j in range(cols):
#         add_row.append(A[i][j] + B[i][j])
#         sub_row.append(A[i][j] - B[i][j])

#     add.append(add_row)
#     subtract.append(sub_row)

# print("A + B =", add)
# print("A - B =", subtract)


# #QN_203
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]

# rows = len(A)
# cols = len(B[0])

# result = []

# for i in range(rows):
#     row = []

#     for j in range(cols):
#         total = 0

#         for k in range(len(B)):
#             total += A[i][k] * B[k][j]

#         row.append(total)

#     result.append(row)

# print(result)


#QN_204
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# n = len(matrix)

# primary_sum = 0
# secondary_sum = 0

# for i in range(n):
#     primary_sum += matrix[i][i]
#     secondary_sum += matrix[i][n - 1 - i]

# print("Primary:", primary_sum)
# print("Secondary:", secondary_sum)


#QN_205
# matrix = [
#     [1, 2],
#     [2, 1]
# ]

# n = len(matrix)
# symmetric = True

# if len(matrix[0]) != n:
#     symmetric = False
# else:
#     for i in range(n):
#         for j in range(n):
#             if matrix[i][j] != matrix[j][i]:
#                 symmetric = False
#                 break
#         if not symmetric:
#             break

# if symmetric:
#     print("Symmetric")
# else:
#     print("Not Symmetric")


#QN_206
# matrix = [
#     [1, 2],
#     [3, 4]
# ]

# n = len(matrix)

# new_matrix = []

# for j in range(n):
#     row = []
#     for i in range(n - 1, -1, -1):
#         row.append(matrix[i][j])
#     new_matrix.append(row)

# print(new_matrix)