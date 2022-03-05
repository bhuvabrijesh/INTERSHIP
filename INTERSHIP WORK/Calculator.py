value1 = int(input("Enter Value 1 : "))
operation = input("Enter Operation : ")
value2 = int(input("Enter Value 2 : "))

if operation== "+":
    print("Sum = {0}".format(value1 + value2))
elif operation=="-":
    print("Substract : {0}".format(value1-value2))
elif operation=="*":
    print("Multiplication : {0}".format(value1*value2))
elif operation=="/":
    print("Division : {0}".format(value1/value2))
elif operation=="%":
    print("Percentage Value : {0}".format((value1*value2)/100))
else:
    print("Invalid Operation")