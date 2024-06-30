import re

test_string = '123ABCabc4567abcABC'

pattern = re.compile(r"abc") # r -> raw string
matches = pattern.finditer(test_string)

for _ in matches:
    print(_)

