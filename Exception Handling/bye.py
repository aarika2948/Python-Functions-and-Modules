valid =False
while not valid:
    try:
        num=int(input("Enter a number:"))
        while num%2==0:
            print("bye")
        valid= True
    except ValueError:
        print("Invalid")
