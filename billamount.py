#1. WAP to calculate the final bill amount along with the discount as per the bill amount.
#Input : Product, Qty, Rate:
#Calculate the bill amount : Qty * Rate
#Bill Amount   Discount Rate
#0-2000              No Discount
#2001-4000           0.05
#4001-6000           0.1
#>6000               0.15

print("To calculate bill amount:-")
product = input("Enter the product:")
quantity = int(input("Enter quantity:"))
rate = int(input("Enter rate per unit:"))
billamount = quantity * rate
print(f"The bill amount will be:{billamount}")
if billamount<=2000:
    print("No Discount")
elif billamount<=4000 and billamount>2000:
    discount = 0.05 * 100
    finalamt = billamount * 0.05
    print(f"{discount}% Discount")
    discamt = billamount - finalamt
    print(f"The final amount will be:{discamt}")
elif billamount<=6000 and billamount>4000:
    discount = 0.1 * 100
    finalamt = billamount * 0.1
    print(f"{discount}% Discount")
    discamt = billamount - finalamt
    print(f"The final amount will be:{discamt}")
else:
    discount = 0.15 * 100
    finalamt = billamount * 0.15
    print(f"{discount}% Discount")
    discamt = billamount - finalamt
    print(f"The final amount will be:{discamt}")

