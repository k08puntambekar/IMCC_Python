import os

filenames = next(os.walk(input("Please provide path of folder : "))) [2]

print("The files in folder are : \n")

print("File Number         File Name")

for file in filenames:
    print(str(filenames.index(file)+1) + "         " + str(file))
