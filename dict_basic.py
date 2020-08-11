purse = dict()

purse['money'] = 12
purse['tissue'] = 75
purse['candy'] = 3

# print(purse)
counts = {'perfect' : 1, 'plan' : 42, 'b': 100}

for key in counts:
    if counts[key] > 10:
        print(key, counts[key])