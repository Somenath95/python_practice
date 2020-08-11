try:
    file = open('file.txt')

except:
    print('Unrecognisable File')    
    quit()

words =[]
for line in file:
    line = line.rstrip()
    new = line.split()
    words.append(new[2])

for word in words:
    print(word)