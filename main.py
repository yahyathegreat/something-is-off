num = 3
if num > 0:
    print(num,"is a positive number.")
num = -1
if num > 0:
    print(num, "is a positve number")



actualcost = float(input("please enter actual product price:"))
saleamount = float (input("please enter sales amount: "))
if (saleamount > actualcost):
    amount = saleamount - actualcost
    print("total profit = {0}". format(amount))
else:
    print("no profit!!!")
    