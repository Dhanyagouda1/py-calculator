
num1=int(input("enter the first number \n"))
num2=int(input("enter the second number\n"))
print("choose the operation\n")
while(1):  
 opr=input("enter '-' for performing subtraction \n enter '+' for performing addition\n enter '*' for performing multiplication\n enter '/' for performing division\n enter 'q' to exit")
 if(opr=='-'):
    print(num1-num2)
 elif(opr=='+'):
    print(num1+num2)
 elif(opr=='*'):
    print(num1*num2)
 elif(opr=='/'):
    print(num1/num2)
 else:
    print("You're exiting from the calculator\n THANK YOU!!")    
    exit(0)
   