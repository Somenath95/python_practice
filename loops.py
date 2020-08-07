num = 0
sum = 0
while True:
   value = input("Enter a number: ")
   if value == 'exit':
       break
   try:
       final_value = float(value)
   except:
       print('Invalid')
       continue
   num = num + 1
   sum = sum + final_value

print(sum,num,sum/num)