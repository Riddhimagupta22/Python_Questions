year = int(input("Enter the value of Year :\n"))

if(year % 400 == 0):
    print("{0} is Leap Year".format(year))
elif(year % 100 == 0 ):
   print("{0} is Non Leap Year".format(year))
elif(year % 4 == 0 ):
   print("{0} is Leap Year".format(year))
else:
    print("{0} is Non Leap Year".format(year))
print("Have a nice day")