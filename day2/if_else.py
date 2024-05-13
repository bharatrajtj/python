import sys

type = sys.argv[1]

if type == "t2.micro":
    print("The EC2 instance comes under Free Tier")

elif type == "t2.medium":
    print("This EC2 instance will be charged")

elif type == "t2.large":
    print("This EC2 instance is expensive")

else:
    print("please provide a valid instance type")
