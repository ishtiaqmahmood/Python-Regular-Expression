import re

test_string = '123ABCabc4567abcABC'

pattern = re.compile(r"abc") # r -> raw string

# match(), search(), findall()
'''
match(): Determine if the RE matches at the beginning of the string.
search(): Scan through a string, looking for any location where this RE matches.
findall(): Find all substrings where the RE matches, and returns them as a list.
finditer(): Find all substrings where the RE matches, and returns them as an iterator.

'''

matches = pattern.findall(test_string)

for _ in matches:
    print(_)

match = pattern.match(test_string) # match() will looking items at the beginning
print(match)

match = pattern.search(test_string) # search() will give the result of 1st findings
print(match)
