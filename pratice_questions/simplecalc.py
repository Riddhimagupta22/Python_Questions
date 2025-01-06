num1 = float(input("Enter the value of num1 :\n"))
num2 = float(input("Enter the value of num2 : \n"))

print("1 : For Addition\n2 : For Subtaction\n3 : For Multiplication\n4 : For Division\n5 : For Modulus\n")

operator = int(input("Enter the operator from (1-5) : "))

if(operator == 1):
    print("Addition of two Number : ",num1 + num2)
elif(operator == 2):
       print("Subtraction of two Number : ",num1 - num2)
elif(operator == 3):
     print("Multiplication of two Number : ",num1*num2)
elif(operator == 4):
    print("Division of two Number : ",num1%num2)
elif(operator == 5):
    print("Modulus of two Number : ",num1/num2)
else :  
    print("Enter a valid Operator")

print("Have a nice day")