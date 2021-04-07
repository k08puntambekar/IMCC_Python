string = "INSTITUTE OF MANAGEMENT AND CAREER COURSES"
string2 = "imcc"

capsString = string.capitalize()
print("First letter Capital : ", capsString)

case_string = string.casefold()
print("Lowercase string : ", case_string)

result = string.endswith('COURSES')
print(result)
result = string.endswith('COURS')
print(result)
result = string.endswith('AND CAREER COURSES')
print(result)

print("isalpha() method : ")
print(string.isalpha())
print(string.isalpha())
