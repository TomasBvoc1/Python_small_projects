import math
repeat = "yes" or "y"

while repeat == "yes" or repeat == "y":
    print("MENU")
    print("If you want to convert km ---> miles, hit 1...")
    print("...if you want to convert miles ---> km, hit 2.")
    x = int(input())
    # print(x)
    # print(type(x))

    if x==1:
        km = float(input("Enter the km value:"))
        miles = km * 0.621371
        print (km, "is equal to ", miles, "miles")
    elif x==2:
        miles = float(input("Enter the miles value:"))
        km = miles / 0.621371
        print (miles, "is equal to ", km, "kilometres")
    else:
        print ("Wrong input, choose again !")
        repeat = "yes"

    repeat = input ("Do you want convert again ? ")
    repeat.lower()
