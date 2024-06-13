print("Welcome to Calculator")
print(" 1.Add\n","2.Subtract\n","3.Multiply\n","4.Divide\n")
option=int(input("Choose an Operation:"))
result=0
if(option in [1,2,3,4]):
     num1=int(input("Enter First Number:"))
     num2 = int(input("Enter Second Number:"))

     if(option==1):
         result=num1+num2
     elif(option==2):
         result=num1-num2
     elif(option==3):
         result=num1*num2
     elif(option==4):
         result=num1//num2
else:
    print("Invalid operation entered")
print("The result of the operation is {}".format(result))
