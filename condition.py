counts =()

names = ['scev', 'sam', 'ram', 'joey', 'happy']
for name in names:
    counts[name] = counts.get(name, 0) + 1

print(counts)    