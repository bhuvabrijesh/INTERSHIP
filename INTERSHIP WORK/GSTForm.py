categoryName = input("Enter Category Name : ")

if categoryName=="Cloth":
    price = int(input("Enter Product Price : "))
    gst = int(input("Enter GST Percentage : "))
    gstAmount = (price*gst)/100
    totalAmount = gstAmount+price
    print("Product Price : {1} & GST Percentage = {0} & GST Amount = {2} & Total Amount = {3}".format(gst,price,gstAmount,totalAmount))
else:
    print("Invalid Category")