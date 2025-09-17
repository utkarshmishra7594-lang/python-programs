'''
n=input("enter the number:")
sum=0
for i in n:
    sum=int(i)+sum
print("sum of digit=",sum)'''  

with open("demo.txt","w+") as f:
    f.write("hi\n")
    f.seek(0)
    print(f.read())
