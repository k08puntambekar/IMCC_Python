firstfile = open('pc-wallpapers-1.jpg', 'rb')
secondfile = open('new.jpg', 'wb')

for line in firstfile:
    secondfile.write(line)

print("File copied")
