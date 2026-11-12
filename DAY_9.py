#61 --> Print every character
text = input()
for c in text:
    print(c)


#62 --> Find the length of a string
text = input()
count = 0
for c in text:
    count += 1
print(count)


#63 --> Reverse a string
text = input()
reversed_string = ""
for i in range(len(text) - 1, -1, -1):
    reversed_string += text[i]
print(reversed_string)


#64 --> Check whether a string is a palindrome
text = input()
rev = ""
for i in range(len(text) - 1, -1, -1):
    rev += text[i]
if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


#65 --> Remove spaces from a string
text = input()
result = ""
for c in text:
    if c != " ":
        result += c
print(result)


#66 --> Convert uppercase to lowercase
text = input()
result = ""
for c in text:
    if 65 <= ord(c) <= 90:
        result += chr(ord(c) + 32)
    else:
        result += c
print(result)


#67 --> Toggle the case of each character
text = input()
result = ""
for c in text:
    if 65 <= ord(c) <= 90:
        result += chr(ord(c) + 32)
    elif 97 <= ord(c) <= 122:
        result += chr(ord(c) - 32)
    else:
        result += c
print(result)


#68 --> Capitalize the first letter of each word
text = input()
new_word = True
result = ""
for c in text:
    if c == " ":
        new_word = True
        result += c
    elif new_word:
        if 97 <= ord(c) <= 122:
            result += chr(ord(c) - 32)
        else:
            result += c
        new_word = False
    else:
        result += c
print(result)


#69 --> Remove vowels from a string
text = input()
result = ""
for c in text:
    if c.lower() not in "aeiou":
        result += c
print(result)


#70 --> Count words in a sentence (or paragraph)
text = input()
count = 0
in_word = False
for c in text:
    if c != " ":
        if not in_word:
            count += 1
            in_word = True
    else:
        in_word = False
print(count)


#71 --> Count vowels and consonants
text = input()
vowels = []
consonants = []
for c in text:
    if c.isalpha():
        if c.lower() in "aeiou":
            vowels.append(c)
        else:
            consonants.append(c)
print("Vowels:", len(vowels), "(" + ", ".join(vowels) + ")")
print("Consonants:", len(consonants), "(" + ", ".join(consonants) + ")")


#72 --> Find the frequency of a character in a string
text = input()
char = input()
count = 0
for c in text:
    if c == char:
        count += 1
print(count)


#73 --> Count the digits, letters and special characters
text = input()
letters = 0
digits = 0
special = 0
for c in text:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        digits += 1
    else:
        special += 1
print("Letters:", letters)
print("Digits:", digits)
print("Special characters:", special)


#74 --> Find duplicate characters in a string
text = input()
dupl_char = []
for i in range(len(text)):
    for j in range(i + 1, len(text)):
        if text[i] == text[j] and text[i] not in dupl_char:
            dupl_char.append(text[i])
print(" ".join(dupl_char))


#75 --> Remove duplicate characters from a string
text = input()
result = ""
for c in text:
    if c not in result:
        result += c
print(result)


#76 --> Find the first non-repeating character
text = input()
for i in range(len(text)):
    count = 0
    for j in range(len(text)):
        if text[i] == text[j]:
            count += 1
    if count == 1:
        print(text[i])
        break


#77 --> Find the first repeating character
text = input()
for i in range(len(text)):
    count = 0
    for j in range(len(text)):
        if text[i] == text[j]:
            count += 1
    if count > 1:
        print(text[i])
        break


#78 --> Find the most frequent character
text = input()
freq_char = {}
for c in text:
    if c in freq_char:
        freq_char[c] += 1
    else:
        freq_char[c] = 1

max_char = ""
max_count = 0
for c in freq_char:
    if freq_char[c] > max_count:
        max_count = freq_char[c]
        max_char = c
print(max_char, "(" + str(max_count), "times)")


#79 --> Print character frequency sorted by count
text = input()
freq_char = {}
for c in text:
    if c in freq_char:
        freq_char[c] += 1
    else:
        freq_char[c] = 1

while len(freq_char) > 0:
    max_char = ""
    max_count = 0
    for c in freq_char:
        if freq_char[c] > max_count:
            max_count = freq_char[c]
            max_char = c
    print(max_char, ":", max_count)
    del freq_char[max_char]


#80 --> Check whether two strings are anagrams
str1 = input()
str2 = input()
if len(str1) != len(str2):
    print("Not Anagram")
else:
    freq_char1 = {}
    freq_char2 = {}
    for c in str1:
        if c in freq_char1:
            freq_char1[c] += 1
        else:
            freq_char1[c] = 1
    for c in str2:
        if c in freq_char2:
            freq_char2[c] += 1
        else:
            freq_char2[c] = 1
    if freq_char1 == freq_char2:
        print("Anagram")
    else:
        print("Not Anagram")


#81 --> Check whether two strings are rotations of each other
str1 = input()
str2 = input()
if len(str1) == len(str2) and str2 in str1 + str1:
    print("Rotation")
else:
    print("Not Rotation")


#82 --> Find the longest word in a sentence
text = input()
freq_char = {}
word = ""
new_word = True

for c in text:
    if c == " ":
        if not new_word:              # a word just ended, so save it
            freq_char[word] = len(word)
            word = ""
        new_word = True
    else:
        word += c
        new_word = False

if not new_word:                      # save the last word
    freq_char[word] = len(word)

max_word = ""
max_len = 0
for w in freq_char:
    if freq_char[w] > max_len:
        max_len = freq_char[w]
        max_word = w

print(max_word)


#83 --> Find the shortest word in a sentence
text = input()
freq_char = {}
word = ""
new_word = True

for c in text:
    if c == " ":
        if not new_word:              # a word just ended, so save it
            freq_char[word] = len(word)
            word = ""
        new_word = True
    else:
        word += c
        new_word = False

if not new_word:                      # save the last word
    freq_char[word] = len(word)

min_word = ""
min_len = float("inf")
for w in freq_char:
    if freq_char[w] < min_len:
        min_len = freq_char[w]
        min_word = w

print(min_word)

#84 --> Reverse each word in a sentence
text = input()
word = ""
new_word = True
result = ""

for c in text:
    if c == " ":
        if not new_word:              # a word just ended, so add it reversed
            if result != "":
                result += " "
            result += word
            word = ""
        new_word = True
    else:
        word = c + word               # put each new letter in front
        new_word = False

if not new_word:                      # add the last word
    if result != "":
        result += " "
    result += word

print(result)


#85 --> Reverse the order of words
text = input()
word = ""
new_word = True
result = ""

for c in text:
    if c == " ":
        if not new_word:              # a word just ended, so put it in front
            if result != "":
                result = word + " " + result
            else:
                result = word
            word = ""
        new_word = True
    else:
        word += c
        new_word = False

if not new_word:                      # add the last word
    if result != "":
        result = word + " " + result
    else:
        result = word

print(result)


#QN_86

# sentence = input().lower()

# letters = set()

# for ch in sentence:
#     if ch >= 'a' and ch <= 'z':
#         letters.add(ch)

# if len(letters) == 26:
#     print("Pangram")
# else:
#     print("Not Pangram")



#QN_87

# s = input()

# result = ""
# count = 1

# for i in range(len(s) - 1):
#     if s[i] == s[i + 1]:
#         count += 1
#     else:
#         result += s[i] + str(count)
#         count = 1


#Final step after the loop
# The loop finishes without adding the final group of b characters, so this line adds it:

# result += s[-1] + str(count)

# print(result)

#QN_88

# words = input().split()

# prefix = words[0]
# for word in words[1:]:
#     while prefix != "":
#         match = True
#         for i in range(len(prefix)):
#             if i >= len(word) or prefix[i] != word[i]:
#                 match = False
#                 break
#         if match:
#             break
#         else:
#             prefix = prefix[:-1]
# print(prefix)


#QN_89
# s = input()
# result = True

# for ch in s:
#     if ch < '0' or ch > '9':
#         result = False
#         break

# print(result)


#QN_90
# s = input()

# s = input()

# for start in range(len(s)):
#     sub = ""
#     for end in range(start, len(s)):
#         sub += s[end]
#         print(sub, end=" ")


#QN_91
# s = input()

# def permutation(current, remaining):
#     if remaining == "":
#         print(current, end=" ")
#         return

#     for i in range(len(remaining)):
#         ch = remaining[i]
#         new_remaining = remaining[:i] + remaining[i + 1:]
#         permutation(current + ch, new_remaining)

# permutation("", s)


#QN_92
# s = input()

# max_length = 0

# for start in range(len(s)):
#     sub = ""

#     for end in range(start, len(s)):
#         if s[end] in sub:
#             break

#         sub += s[end]

#         if len(sub) > max_length:
#             max_length = len(sub)

# print(max_length)


#QN_93
# s = input()

# longest = ""

# for start in range(len(s)):
#     sub = ""

#     for end in range(start, len(s)):
#         sub += s[end]

#         left = 0
#         right = len(sub) - 1
#         is_palindrome = True

#         while left < right:
#             if sub[left] != sub[right]:
#                 is_palindrome = False
#                 break

#             left += 1
#             right -= 1

#         if is_palindrome and len(sub) > len(longest):
#             longest = sub

# print(longest)


#QN_94
# s = input()

# result = 0

# for ch in s:
#     digit = ord(ch) - ord('0')
#     result = result * 10 + digit

# print(result)