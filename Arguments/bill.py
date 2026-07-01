def bill(bill_amt, tip_perc):
    total=bill_amt*(1+((tip_perc)/100))
    total=round(total, 2)
    return total
x=int(input("Enter the amount of the bill="))
y=int(input("Enter the tip percent="))
print(f"The total amount is {bill(x, y)}")