def read_lines(file_name):
    f = open(file_name)
    l = f.readlines()

    for lines in l:
        print(lines)


read_lines("DemoText.txt")
