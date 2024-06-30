import re

test_string = '123ABCabc4567abcABC'

pattern = re.compile(r"abc") # r -> raw string
matches = pattern.finditer(test_string)

#for _ in matches:
    #print(_)

# group, start, end, span
for match in matches:
    
    print("Start: {}".format(match.start()))
    print("End: {}".format(match.end()))
    print("Span : {}".format(match.span()))
    print("Group: {}".format(match.group()))