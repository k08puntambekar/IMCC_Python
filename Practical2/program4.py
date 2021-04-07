def display_words():
    count = 0
    file = open("DemoText.txt", "r")
    lines = file.read()
    word = lines.split()

    for words in word:
        if len(words) < 4:
            count += 1
            print(words, end=",")

    print()
    print("Total number of words having characters less than 4 are : ", count)

display_words()
    
