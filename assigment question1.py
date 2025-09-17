num1=int(input("enter first number :"))
num2=int(input("enter second number :"))
if num2>num1:
    smallar=num1
else:
    smallar=num2
    
for i in range(1,smallar+1):
    if((num1%i==0) and (num2%i==0)):
        GCD=i     
        
print("GCD is=",GCD)


