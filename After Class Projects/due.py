payed_amt=float(input("Enter the amount payed="))
bill_sum=float(input("Enter the amount of the bill="))
if (payed_amt>bill_sum):
    print("The shopkeeper has to return to the customer", payed_amt-bill_sum)
elif(payed_amt==bill_sum):
    pass
else:
    print("The customer has to return to the shopkeeper", bill_sum-payed_amt)