def ReadLines(fileName):
    f = open(fileName)
    l = f.readlines()

    for lines in l:
        print(lines)

ReadLines("DemoText.txt")
