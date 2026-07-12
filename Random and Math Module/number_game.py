import random
print("I will generate a number between 0 to 9. Try your best to guess it.")
num=(random.randint(0,9))
tries=0
while True:
    guess=int(input("Enter your guess="))
    tries+=1
    if guess==num:
        print("You got it right. The number is", guess, "You guess it in ",tries, "tries." )
        break
    else:
        print("You are wrong. Try again!")
        continue
