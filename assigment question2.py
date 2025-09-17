num=int(input("enter the number:"))
fact=1
for i in range(1,num+1):
    fact=i*fact
    i=i+1
    
print("factorial of the num=",fact)