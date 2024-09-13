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


i = int (input("enter a number : "))
if (i < 15):
    print(" i is smaller  than 15")
    print("i'm in if block")
else:
    print (" i is greater than 15")
    print (" i'm in else block")
print ("i'm not in if and not in else block")


number = int(input("enter number to check"))

if number%2==0 :
    print ("this is an even number")

else:
    print("this is a odd number")
    