Time=float(input("enter the time (hh.mm):"))
if 0<Time<12:
   print("good morning")

elif 12<=Time<16:
   print("good afternoon")

elif 16<=Time<20:
   print("good evening")
elif 20<=Time<24:
   print("Good night")

else:
  print("enter a valide time(hh.mm)")   
