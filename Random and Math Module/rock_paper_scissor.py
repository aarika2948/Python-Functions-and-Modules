import random
print("This is a rock, paper, scissor.")
round=int(input("Enter the number of rounds you want="))
scoreh=0
scorer=0
round_n=1
options=["rock", "paper", "scissor"]
for i in range(1, round+1):
    print(f"Round {round_n}")
    robot=(random.choice(options))
    human=input("Enter your choice=").lower()
    if human not in options:
        print("Invalid Input")
        continue
    if (robot=="rock" and human=="paper"):
        scoreh+=1
        print("You Won!")
    elif (robot=="rock" and human=="scissor"):
        scorer+=1
        print("You Lost!")
    elif (robot=="paper" and human=="scissor"):
        scoreh+=1
        print("You Won!")
    elif (robot=="paper" and human=="rock"):
        scorer+=1
        print("You Lost!")
    elif (robot=="scissor" and human=="rock"):
        scoreh+=1
        print("You Won!")
    elif (robot=="scissor" and human=="paper"):
        scorer+=1
        print("You Lost!")
    else:
        print("Its a tie")
    round_n+=1
print("The final scores are:")
print(f"Your score:{scoreh}")
print(f"Robot's score:{scorer}")
if scoreh>scorer:
    print("You won by", scoreh-scorer, "points")
elif scorer>scoreh:
    print("You lost by", scorer-scoreh, "points")
else:
    print("Its a tie.")




