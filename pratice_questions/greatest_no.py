num1 = int(input("Enter the value of num1 :\n"))
num2 = int(input("Enter the value of num2 : \n"))
num3 = int(input("Enter the value of num3 : \n"))

if( num1 > num2 and num1 > num3 ):
    print("{0} is Greatest Number".format(num1))
elif( num2 > num1 and num2 > num3 ):
    print("{0} is Greatest Number".format(num2)) 
else:
    print("{0} is Greatest".format(num3))   

print("Thank You")