print("--------- ELECTRICITY BILL CALCULATOR ---------")

unit = int(input("Enter Total Units : "))

if unit <= 100:
    bill = unit * 6

elif unit <= 200:
    bill = (100 * 6) + ((unit - 100) * 7)

elif unit <= 300:
    bill = (100 * 6) + (100 * 7) + ((unit - 200) * 8)

else:
    bill = (100 * 6) + (100 * 7) + (100 * 8) + ((unit - 300) * 10)

fixed_charge = 200
tax = bill * 10 / 100
total_bill = bill + fixed_charge + tax

print()
print("----------- ELECTRICITY BILL -----------")
print("Units Consumed :", unit)
print()

if unit <= 100:
    print("1 - 100 Per Unit ₹6 =", bill)

elif unit <= 200:
    print("1 - 100 Per Unit ₹6 =", 100 * 6)
    print("101 - 200 Per Unit ₹7 =", (unit - 100) * 7)

elif unit <= 300:
    print("1 - 100 Per Unit ₹6 =", 100 * 6)
    print("101 - 200 Per Unit ₹7 =", 100 * 7)
    print("201 - 300 Per Unit ₹8 =", (unit - 200) * 8)

else:
    print("1 - 100 Per Unit ₹6 =", 100 * 6)
    print("101 - 200 Per Unit ₹7 =", 100 * 7)
    print("201 - 300 Per Unit ₹8 =", 100 * 8)
    print("301 - Above Per Unit ₹10 =", (unit - 300) * 10)

print()
print("Electricity Charge : ₹", bill)
print("Fixed Charge : ₹", fixed_charge)
print("Tax (10%) : ₹", tax)
print("Total Bill : ₹", total_bill)
print("----------------------------------------")
