try:
    fhand = open('file.txt')
except:
    print("Unsupported file")
    quit()

for line in fhand:
    line = line.rstrip()
    print(line.upper())