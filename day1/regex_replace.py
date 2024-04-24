import re

stat = "DevOps is the way"
find = "DevOps"

change = "AWS"

sw = re.sub(find, change, stat)
print("Truth:", sw)
