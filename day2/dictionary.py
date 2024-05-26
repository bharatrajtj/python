#### List of Dictionaries

ec2_details = [
    {
        "Region": "Us-east-1",
        "type": "t2.micro"
    },

    {
        "Region": "Us-east-2",
        "type": "t2.small"
    },

    {
        "Region": "Us-west-1",
        "type": "t2.large"
    },

    {
        "Region": "Us-east-1",
        "type": "t2.micro"
    }

]

print(ec2_details[1]["type"])    #### First is used to select the dictionary from the indexed list. 
                                 ####Second is used to select key from the selected dictionary
