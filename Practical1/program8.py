def count(string):
    vowels = 0
    characters = 0
    number = 0
    spaces = 0

    for i in range(0, len(string)):

        ch = string[i]

        if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
            characters += 1
            # ch = ch.lower()

            if (ch == 'a' or ch == 'e' or ch == 'i'
                    or ch == 'o' or ch == 'u'):
                vowels += 1

        elif ch >= '0' and ch <= '9':
            number += 1

        elif string[i] == " ":
            spaces += 1

    print("Vowels : ", vowels)
    print("Characters : ", characters)
    print("Number : ", number)
    print("Spaces : ", spaces)


string = "Practical program no 08"
count(string)
