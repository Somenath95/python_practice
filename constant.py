def computeTotalPay(days, roi):
    total_income = days * roi
    return total_income

days = input("Enter days:" )
roi = input("Enter rate per day: ")

try:    
    days = int(days)
    roi = float(roi)
    total_income = computeTotalPay(days, roi)
    print("Pay: ",total_income)

except:
    print("Error, Please Enter Numeric Input")