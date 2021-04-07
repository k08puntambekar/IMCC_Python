def findTheLine(lineNo):
    file = open("DemoLineText.txt")
    lines = file.readlines()
    print(lines[lineNo-1])

findTheLine(4)
