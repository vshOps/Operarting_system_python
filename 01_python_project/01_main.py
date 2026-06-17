'''
snake = -1
water = 1
gun = 0'''
import random
computer = random.choice([1,0,-1])

print(f"s for 🐍\nw for 💧\ng for 🔫")

youstr = input("Enter your choice: ")
youDict = {"s":-1, "w":1, "g":0}
you = youDict[youstr]
reverseDict = {-1:"Snake", 1:"Water", 0:"Gun"}

print(f"Computer chose: {reverseDict[computer]} \nYou chose: {reverseDict[you]}")

if computer==you:
    print("It's a tie!")
else:
    if computer==-1 and you==1:
        print("Computer wins!")
    elif computer==-1 and you==0:
        print("You win!")
    elif computer==1 and you==-1:
        print("You win!")
    elif computer==1 and you==0:
        print("Computer wins!")
    elif computer==0 and you==1:
        print("You win!")
    elif computer==0 and you==-1:
        print("Computer wins!")
    else:
        print("Something went wrong!")