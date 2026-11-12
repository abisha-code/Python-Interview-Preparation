#QN_39
num = int(input())
binary = ""

if num == 0:
    binary = "0"

while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary
    num //= 2

print(binary)

#QN_41

num=int(input())
octal=""

if num==0:
    print("0")

while num>0:
    rem=num%8
    octal=str(rem)+octal
    num//=8

print(octal)


num=int(input())
hexadecimal=""
chars="0123456789ABCDEF"


if num==0:
    print("0")

while num>0:
    rem=num%16
    hexadecimal=chars[rem]+hexadecimal
    num//=16

print(hexadecimal)


#QN_42
num = int(input())
count = 0
while num > 0:
    count += num % 2
    num //= 2
print(count)
