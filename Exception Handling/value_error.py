try:
    num=int(input("Enter the number= "))
    print(f"The number is {num}")
except ValueError as ex:
    print(f"Exception:{ex}")