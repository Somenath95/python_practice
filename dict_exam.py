try:
    file = open('file.txt')
except:
    print('Unrecognisable file')
    quit()

counts = dict()
# words = []
for line in file:
    line = line.rstrip()    
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# print('Words: ',words)
print('Counts: ',counts)

largest = -1
key_word = None
for key,value in counts.items():
    print(key, value)
    if value > largest:
        largest = value
        key_word =key

print("\nThe Largest:", key_word, largest)     
