#Defining all functions for the operations
def add(x, y):
    return(x+y)
def sub(x, y):
    return(x-y)
def pro(x, y):
    return(x*y)
def div(x, y):
    return(x/y)
def value():
    try:
        x=float(input("Enter the first value="))
        y=float(input("Enter the second value="))
        print("a:Addition\nb:Subtraction\nc:Multiplication\nd:Division")
        op=input("Enter the desired opperation (a/b/c/d)=").lower()
        if len(op)>1 or op not in ["a", "b", "c", "d"]:
            print("Invalid Input!")
        elif op=="a":
            print(f"{x}+{y}={add(x, y)}")
        elif op=="b":
            print(f"{x}-{y}={sub(x, y)}")
        elif op=="c":
            print(f"{x}*{y}={pro(x, y)}")
        elif op=="d":
            print(f"{x}/{y}={div(x, y)}")
    except ValueError as v:
        print(f"Exception:{v}, Your input isn't a number.")
        value()
    except ZeroDivisionError as z:
        print(f"Exception:{z}, You can't divide a numbr by 0.")
        value()

value()





    

