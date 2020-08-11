dic = {'a':10, 'c':50, 'b':40}
t = sorted(dic.items())
print(t)

tmp = list()
for k,v in dic.items():
    tmp.append((v, k))
print(tmp)

tmp = sorted(tmp, reverse=False)
print(tmp)