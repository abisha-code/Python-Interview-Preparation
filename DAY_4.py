#QN_31
# num = int(input())

# if num <= 1:
#     print("Not a Prime Number")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a Prime Number")
#             break
#     else:
#         print("Prime Number")


#QN_32
a, b = map(int, input().split())
for num in range(a, b + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")

"""
Step 1: Outer loop iteration
range(a, b + 1) means range(1, 6), which generates 1, 2, 3, 4, 5.


Iteration 1: num = 1
- num <= 1 → 1 <= 1 → True
- continue skips the remaining code and moves to the next number.
Output: Nothing.


Iteration 2: num = 2
- num <= 1 → False
- Inner loop: range(2, 2) is empty, so it does not execute.
- The inner for-else executes because no break occurred.
- Prints 2.
Output: 2


Iteration 3: num = 3
- num <= 1 → False
- Inner loop: range(2, 3) gives 2.
- 3 % 2 == 0 → False.
- No break occurs, so the else executes.
- Prints 3.
Output: 2 3


Iteration 4: num = 4
- num <= 1 → False
- Inner loop: range(2, 4) gives 2, 3.
- When i = 2, 4 % 2 == 0 → True.
- break stops the inner loop.
- The inner else does not execute, so 4 is not printed.
Output: 2 3


Iteration 5: num = 5
- num <= 1 → False
- Inner loop: range(2, 5) gives 2, 3, 4.
- None of these numbers divides 5 exactly.
- No break occurs, so the else executes.
- Prints 5.
Output: 2 3 5

"""

#QN_33
n = int(input())
primes = []
num = 2
while len(primes) < n:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    num += 1
print(*primes)


"""
Step-by-step iteration
Initial values:
- n = 5
- primes = []
- num = 2



Iteration 1 — num = 2
- while len(primes) < n → 0 < 5 → True
- is_prime = True
- range(2, 2) is empty, so the for loop does not execute.
- is_prime remains True.
- primes.append(2) adds 2 to the list.
- num += 1 → num = 3
Result: primes = [2]



Iteration 2 — num = 3
- len(primes) < n → 1 < 5 → True
- is_prime = True
- range(2, 3) gives 2.
- 3 % 2 != 0, so is_prime remains True.
- Append 3 to the list.
- num += 1 → num = 4
Result: primes = [2, 3]



Iteration 3 — num = 4
- len(primes) < n → 2 < 5 → True
- is_prime = True
- range(2, 4) gives 2, 3.
- When i = 2, 4 % 2 == 0.
- is_prime = False, and break stops the for loop.
- Since is_prime is False, 4 is not appended.
- num += 1 → num = 5
Result: primes = [2, 3]



Iteration 4 — num = 5
- len(primes) < n → 2 < 5 → True
- is_prime = True
- range(2, 5) gives 2, 3, 4.
- None of these numbers divides 5 exactly.
- Append 5 to the list.
- num += 1 → num = 6
Result: primes = [2, 3, 5]



Iteration 5 — num = 6
- len(primes) < n → 3 < 5 → True
- is_prime = True
- range(2, 6) gives 2, 3, 4, 5.
- When i = 2, 6 % 2 == 0.
- is_prime = False, and break stops the loop.
- 6 is not appended.
- num += 1 → num = 7
Result: primes = [2, 3, 5]



Iteration 6 — num = 7
- len(primes) < n → 3 < 5 → True
- is_prime = True
- range(2, 7) gives 2, 3, 4, 5, 6.
- None divides 7 exactly.
- Append 7 to the list.
- num += 1 → num = 8
Result: primes = [2, 3, 5, 7]



Iteration 7 — num = 8
- len(primes) < n → 4 < 5 → True
- is_prime = True
- When i = 2, 8 % 2 == 0.
- is_prime = False, and break stops the loop.
- 8 is not appended.
- num += 1 → num = 9
Result: primes = [2, 3, 5, 7]



Iteration 8 — num = 9
- len(primes) < n → 4 < 5 → True
- is_prime = True
- When i = 3, 9 % 3 == 0.
- is_prime = False, and break stops the loop.
- 9 is not appended.
- num += 1 → num = 10
Result: primes = [2, 3, 5, 7]



Iteration 9 — num = 10
- len(primes) < n → 4 < 5 → True
- is_prime = True
- When i = 2, 10 % 2 == 0.
- is_prime = False, and break stops the loop.
- 10 is not appended.
- num += 1 → num = 11
Result: primes = [2, 3, 5, 7]



Iteration 10 — num = 11
- len(primes) < n → 4 < 5 → True
- is_prime = True
- None of the numbers from 2 to 10 divides 11 exactly.
- Append 11 to the list.
- num += 1 → num = 12
Result: primes = [2, 3, 5, 7, 11]
"""


#QN_34
num = int(input())
factors = []
factor = 2
while num > 1:
    if num % factor == 0:
        factors.append(factor)
        num //= factor
    else:
        factor += 1
print(*factors)


#QN_35
a, b = map(int, input().split())
while b != 0:
    remainder = a % b
    a = b
    b = remainder
print(a)


# #QN_36
a, b = map(int, input().split())
x = a
y = b
while y != 0:
    remainder = x % y
    x = y
    y = remainder
gcd = x
lcm = (a * b) // gcd
print(lcm)


#QN_37
a, b = map(int, input().split())
power = 1
for i in range(abs(b)):
    power = power * a
if b < 0:
    power = 1 / power
print(power)



#QN_38
num = int(input())
if num <= 0:
    print("Not a power of 2")
else:
    while num % 2 == 0:
        num //= 2
    if num == 1:
        print("Power of 2")
    else:
        print("Not a power of 2")


