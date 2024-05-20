#### Input Keyword is used to get input at run time

folders = input("Give the name of the folders:")
print(folders)

###Split is used to convert the string input into a list
folders = input("Give the name of the folders:").split()
print(folders)

###For loop the values of folders is stored in folder
folders = input("please provide list of folders name:  ").split()

for folder in folders:
    print(folder)

###OS module

import os   ### used to interact with OS

folders = input("please provide list of folders name:  ").split()

for folder in folders:
    files = os.listdir(folder)   ### .listdir is a keyword
    print("listing files for the folder" + folder)    ### folder variable is used to store values from folders in FIFO
    print(files)   ### ouptut will be folders in a list sequence

###printing in order

import os

folders = input("please provide list of folders name:  ").split()

for folder in folders:
    files = os.listdir(folder)
    print("listing files for the folder" + folder)

for file in files:
  print(file)

####Exceptional Handling

import os

folders = input("please provide list of folders name:  ").split()

for folder in folders:
  try:
    files = os.listdir(folder)
  except FileNotFoundError:
     print("not valid name")
     break    ### use continue to continue the loop

  print("list of folders-----" + folder)

  for file in files:
    print(file)
