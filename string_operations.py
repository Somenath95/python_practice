# data = 'From jyoti.perfectplanb@uct.ac.za Sat Jan 5 09:14:16 2008'
# pos = data.find('.')
# print(data[pos:pos+3])

# x ='51'
# y = int(x) + 2
# print(y)

# for let in 'perfectplanb':
#     print(let)

str = 'Perfect-Plan-B:0.7541'
part = str.split(':')
print(float(part[1]))