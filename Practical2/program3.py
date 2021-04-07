def occuranceWords():
    file = open("DemoText.txt", "rt")
    data = file.read()
    occurences = data.count("python")

    print("No of times python occurred : ", occurences)

occuranceWords()
