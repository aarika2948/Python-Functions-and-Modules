try:
    num_1, num_2 = eval(input("Enter the numbers, seperated by a comma= "))
    result=num_1/num_2
    print(f"Result:{result}")
except ZeroDivisionError as z:
    print(f"Exception:{z}")
except SyntaxError as s:
    print(f"Exception:{s}")
except:
    print("Wrong Input")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what")