###This is basic demo for regular expression function

import re

#### r before the string treats the string as a raw string
filepath = r"C:\Users\Bharat\Documents\example.txt"
pattern = r"Bharat"

find =  re.search(pattern, filepath)
if find:
    print("User is:", find.group())    ####search will return lot of data, use group() to get the pattern youn declared
    #### if more than one pattern group(1), group (2) 
else:
    print("Not found")
