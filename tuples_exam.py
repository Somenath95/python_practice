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

tmp =list()
for key,value in counts.items():
    new_tup = (value,key)
    tmp.append(new_tup)

tmp = sorted(tmp, reverse=True)

for value,key in tmp:
    print(key, value)
