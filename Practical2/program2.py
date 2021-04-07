def wordCount():
    file = open("DemoText.txt", "rt")
    data = file.read()
    count = data.split()

    print('Number of words in the file :', len(count))

wordCount()
