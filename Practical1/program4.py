number = int(input("Enter a number : "))
reverse = 0

while number > 0:
    temp = number % 10
    reverse = reverse * 10 + temp
    number = number // 10

print("Reverse of a number is : ", reverse)
