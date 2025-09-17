import random
choice1=random.choice(["rock","paper","scissors"])
choice2=input(" chose any one from(rock ,paper ,scissors)")
win=0
los=0
tie=0

while choice2!="quit":
    if choice1=="rock" and choice2=="paper" or choice1=="paper" and choice2=="scissors" or choice1=="scissors" and choice2=="rock":
        print("you have won")
        win+=1
        break
    elif choice1=="paper"and choice2=="rock"or choice1=="scissor"and choice2=="paper" or choice1=="roc;k"and "scissors":
        print("you have lost")
        los+=1
        break
    elif choice1==choice2:
        print("it's tie")
        tie+=1
        break

print(win,los,tie)


