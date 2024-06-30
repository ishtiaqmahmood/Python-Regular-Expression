'''

Special Sequences¶

A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

\d :Matches any decimal digit; this is equivalent to the class [0-9].
\D : Matches any non-digit character; this is equivalent to the class [^0-9].
\s : Matches any whitespace character;
\S : Matches any non-whitespace character;
\w : Matches any alphanumeric (word) character; this is equivalent to the class [a-zA-Z0-9_].
\W : Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].
\b Returns a match where the specified characters are at the beginning or at the end of a word r"\bain" r"ain\b"
\B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word r"\Bain" r"ain\B"
\A Returns a match if the specified characters are at the beginning of the string "\AThe"
\Z Returns a match if the specified characters are at the end of the string "Spain\Z"

'''

import re


# \A -> Returns a match if the specified characters are at the beginning of the string

txt = "The rain in Spain. I love rainning"

# Check if the string starts with "The":

x = re.findall("\AThe", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")

# \b -> Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")

txt = "The rain in Spain"

# Check if "ain" is present at the beginning of a WORD:

x = re.findall(r"\bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

txt = "The rain in Spain"

# Check if "ain" is present at the end of a WORD:

x = re.findall(r"ain\b", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# \B -> Returns a match where the specified characters are present, 
# but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")

txt = "The rain in Spain"

# Check if "ain" is present, but NOT at the beginning of a word:

x = re.findall(r"\Bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

txt = "The rain in Spain"

# Check if "ain" is present, but NOT at the end of a word:

x = re.findall(r"ain\B", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# \d -> Returns a match where the string contains digits (numbers from 0-9)

txt = "The rain in Spain 101"

# Check if the string contains any digits (numbers from 0-9):

x = re.findall("\d", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# \D -> Returns a match where the string DOES NOT contain digits

txt = "The rain in Spain"

# Return a match at every no-digit character:

x = re.findall("\D", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# \s -> Returns a match where the string contains a white space character

txt = "The rain in Spain"

# Return a match at every white-space character:

x = re.findall("\s", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# \S -> Returns a match where the string DOES NOT contain a white space character

txt = "The rain in Spain"

# Return a match at every NON white-space character:

x = re.findall("\S", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# \w -> Returns a match where the string contains
#  any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)

txt = "The rain in Spain"

# Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

x = re.findall("\w", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# \W -> Returns a match where the string DOES NOT contain any word characters

txt = "The rain in Spain"

# Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):

x = re.findall("\W", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# \Z -> Returns a match if the specified characters are at the end of the string

txt = "The rain in Spain"

#Check if the string ends with "Spain":

x = re.findall("Spain\Z", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")

