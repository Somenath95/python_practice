counts = dict()
line = input('Enter a line: ')
words = line.split()

print('Words: ',words)
print('COunting...')

for word in words:
    counts[word] = counts.get(word, 0) +1

print('Counts', counts)