year=int(input("enter the year"))

if (year%4==0) and (year%100!=0):
    print(year,"is leap year")

elif (year%100==0) and(year%400==0):
    print(year,"is leap year")


else:
    print("Not leap year")
    