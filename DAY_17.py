#QN_209
a, b, operator = input().split()

a = int(a)
b = int(b)

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
else:
    print("Invalid operator")


#QN_210
class Bank:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Balance:", self.balance)
        else:
            print("Insufficient balance")


account = Bank(1000)
account.withdraw(400)

#QN_211
marks = list(map(int, input().split()))

total = 0

for mark in marks:
    total += mark

average = total / len(marks)

if average >= 80:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "F"

print("Total:", total)
print("Average:", average)
print("Grade:", grade)


#QN_212
units = int(input())

if units <= 100:
    bill = units * 5
else:
    bill = (100 * 5) + ((units - 100) * 7)

print("Bill:", bill)

#QN_213
class Employee:
    def __init__(self, basic):
        self.basic = basic

    def calculate_salary(self):
        hra = self.basic * 10 / 100
        da = self.basic * 5 / 100

        salary = self.basic + hra + da

        print("Salary:", int(salary))


emp = Employee(30000)
emp.calculate_salary()


#QN_214
celsius = float(input())

fahrenheit = (celsius * 9 / 5) + 32

print(fahrenheit)

#QN_215
username = input()
password = input()

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")


#QN_216
password = input()

has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in password:
    if ch >= 'A' and ch <= 'Z':
        has_upper = True

    elif ch >= 'a' and ch <= 'z':
        has_lower = True

    elif ch >= '0' and ch <= '9':
        has_digit = True

    else:
        has_special = True

if (len(password) >= 8 and has_upper and has_lower
    and has_digit and has_special):
    print("Strong Password")
else:
    print("Weak Password")


#QN_217
date = input()

year, month, day = map(int, date.split("-"))

days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]

month_days = [31, 28, 31, 30, 31, 30,
              31, 31, 30, 31, 30, 31]

# Count leap years from 2024 to the previous year
leap_days = 0

for y in range(2024, year):
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        leap_days += 1

# Count days from previous years
total_days = (year - 2024) * 365 + leap_days

# Count days from previous months
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    month_days[1] = 29

for i in range(month - 1):
    total_days += month_days[i]

# Count days in the current month
total_days += day - 1

# 1 January 2024 was Monday (index 0)
result = total_days % 7

print(days[result])



#QN_218
num = int(input())
#This program handles numbers from 1 to 999. It can be extended to handle thousands and larger numbers too.

ones = ["", "One", "Two", "Three", "Four", "Five",
        "Six", "Seven", "Eight", "Nine"]

teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
         "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty",
        "Sixty", "Seventy", "Eighty", "Ninety"]

result = ""

if num >= 100:
    result += ones[num // 100] + " Hundred"
    num = num % 100

if num >= 20:
    result += " " + tens[num // 10]
    num = num % 10

    if num > 0:
        result += "-" + ones[num]

elif num >= 10:
    result += " " + teens[num - 10]

elif num > 0:
    result += " " + ones[num]

print(result.strip())