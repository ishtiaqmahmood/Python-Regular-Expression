'''
Sets¶

A set is a set of characters inside a pair of square brackets [] with a special meaning. Append multiple conditions back-to back, e.g. [aA-Z].
A ^ (caret) inside a set negates the expression.
A - (dash) in a set specifies a range if it is in between, otherwise the dash itself.

Examples:
- [arn] Returns a match where one of the specified characters (a, r, or n) are present
- [a-n] Returns a match for any lower case character, alphabetically between a and n
- [^arn] Returns a match for any character EXCEPT a, r, and n
- [0123] Returns a match where any of the specified digits (0, 1, 2, or 3) are present
- [0-9] Returns a match for any digit between 0 and 9
- [0-5][0-9] Returns a match for any two-digit numbers from 00 and 59
- [a-zA-Z] Returns a match for any character alphabetically between a and z, lower case OR upper case

'''

import re


# [arn] -> Returns a match where one of the specified characters (a, r, or n) is present

txt = "The rain in Spain"

# Check if the string has any a, r, or n characters:

x = re.findall("[arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# [a-n] -> Returns a match for any lower case character, alphabetically between a and n

txt = "The rain in Spain"

# Check if the string has any characters between a and n:

x = re.findall("[a-n]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# [^arn] -> Returns a match for any character EXCEPT a, r, and n

txt = "The rain in Spain"

# Check if the string has other characters than a, r, or n:

x = re.findall("[^arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# [0123] -> Returns a match where any of the specified digits (0, 1, 2, or 3) are present

txt = "The rain in Spain"

# Check if the string has any 0, 1, 2, or 3 digits:

x = re.findall("[0123]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# [0-9] -> Returns a match for any digit between 0 and 9

txt = "8 times before 11:45 AM"

# Check if the string has any digits:

x = re.findall("[0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# [0-5][0-9] -> Returns a match for any two-digit numbers from 00 and 59

txt = "8 times before 11:45 AM"

# Check if the string has any two-digit numbers, from 00 to 59:

x = re.findall("[0-5][0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# [a-zA-Z] -> Returns a match for any character alphabetically between a and z, lower case OR upper case

txt = "8 times before 11:45 AM"

# Check if the string has any characters from a to z lower case, and A to Z upper case:

x = re.findall("[a-zA-Z]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# [+] -> In sets, +, *, ., |, (), $,{} has no special meaning, 
# so [+] means: return a match for any + character in the string

txt = "8 times before 11:45 AM"

#Check if the string has any + characters:

x = re.findall("[+]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

