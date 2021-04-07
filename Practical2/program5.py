def lastAlphabet():
    count = 0
    last = 'e'
    file = open("DemoText.txt", "r")
    lines = file.readlines()

    for line in lines:
        words = line.split()

        for word in words:
            if word[-1] == last:
                count += 1
                print("Words ending with 'e' : ", count)

lastAlphabet()
