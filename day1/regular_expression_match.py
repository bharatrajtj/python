###This is basic demo for regular expression Match function
###Match looks for the given input is present at the beginning of the string

import re

dan = "aws is awesome"
atr = r"aws"   ### if "is" was given then the result is not found

rest = re.match(atr, dan)
if rest:
    print("It is", rest.group())
else:
    print("not found")
