days = input("Enter days:" )
roi = input("Enter rate per day: ")

try:    
    days = int(days)
    roi = float(roi)
    total_income = days * roi
    print("The rate of interest is: ",total_income)

except:
    print("Error, Please Enter Numeric Input")