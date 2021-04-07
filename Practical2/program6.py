import pickle
filename = "student.dat"
file = open(filename, "wb")

data=[{
    'rollno':11,
    'name':'Aditya',
    'class':'MCA',
    'fees':12445},

    {'rollno':102,
    'name':'Rajesh',
    'class':'MBA',
    'fees':124453},

    {'rollno':103,
    'name':'Sahil',
    'class':'Temp',
    'fees':34556},

    {'rollno':104,
    'name':'Reema',
    'class':'MCA',
    'fees':67445}
      
    ]

pickle.dump(data, file)
file.close()

print("Success")

infile = open(filename, 'rb')
dictlist = pickle.load(infile)
infile.close()

for dict1 in dictlist:
    if(dict1["rollno"] == 11):
        print("Student with Roll no 11 is => , Name : {} | Class : {} | Fees{}"
              .format((dict1["name"]), (dict1["class"]), dict1["fees"]))
