def cube(num):
    c=num**3
    return c
def three(num):
    if num%3==0:
        return cube(num)
    else:
        return False
x=int(input("Enter the number="))
print(three(x))