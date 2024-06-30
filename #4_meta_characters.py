'''

Meta characters

Metacharacters are characters with a special meaning:
All meta characters: . ^ $ * + ? { } [ ] \ | ( )
Meta characters need need to be escaped (with ) if we actually want to search for the char.

. Any character (except newline character) "he..o"
^ Starts with "^hello"
\$ Ends with "world\$"
* Zero or more occurrences "aix*"
+ One or more occurrences "aix+"
{ } Exactly the specified number of occurrences "al{2}"
[] A set of characters "[a-m]"
\ Signals a special sequence (can also be used to escape special characters) "\d"
| Either or "falls|stays"
( ) Capture and group


'''

import re

txt = "The rain in Spain"

# [] -> A set of characters
# Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)

# \ -> Signals a special sequence (can also be used to escape special characters)

txt = "That will be 59 dollars"

# Find all digit characters:

x = re.findall("\d", txt)
print(x)

# . -> Any character (except newline character)

txt = "hello planet"

# Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)

# ^ -> Starts with

txt = "hello planet, hello"

# Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")  

print(x)

# $ -> Ends with

txt = "hello planet"

# Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")

print(x)

# * -> Zero or more occurrences

txt = "welcome to the planet earth. hello planet, hello. I am a dumb boy."

# Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*o", txt)

print(x)

# + -> One or more occurrences

txt = "welcome to the planet earth. hello planet, hello. I am a dumb boy."

# Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

x = re.findall("he.+o", txt)

print(x)

# ? -> Zero or one occurrences

txt = "welcome to the planet earth. hello planet, hello. I am a dumb boy."

# Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

x = re.findall("he.?o", txt)

print(x)

# This time we got no match, because there were not zero, not one, 
# but two characters between "he" and the "o"

# {} -> Exactly the specified number of occurrences

txt = "welcome to the planet earth. hello planet, hello. I am a dumb boy."

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)

print(x)

# | -> Either or

txt = "The rain in Spain falls mainly in the plain!"

# Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


