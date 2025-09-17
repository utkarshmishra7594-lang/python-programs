num1=int(input("enter first number :"))#x=number1
num2=int(input("enter second number :"))#y=number2
if num2>num1:
    smallar=num1
    
else:
    smallar=num2
    

for i in range(1,smallar+1):
    if((num1%i==0) and (num2%i==0)):
        GCD=i     
        
print("GCD is=",GCD)

