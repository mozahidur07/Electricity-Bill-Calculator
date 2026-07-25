def format_amount(value):
    return str(int(value)) if value == int(value) else f"{value:.2f}"


units = int(input("Enter Total Units : "))

slab_1 = min(units, 100) * 6
slab_2 = min(max(units - 100, 0), 100) * 7
slab_3 = min(max(units - 200, 0), 100) * 8
slab_4 = max(units - 300, 0) * 10

electricity_charge = slab_1 + slab_2 + slab_3 + slab_4
fixed_charge = 200
tax = electricity_charge * 10 / 100
total_bill = electricity_charge + fixed_charge + tax

print("--------- ELECTRICITY BILL ---------")
print()
print(f"Units Consumed : {units}")
print()
print(f"1 - 100 Per Unit ₹6 = {format_amount(slab_1)}")
print(f"101 - 200 Per Unit ₹7 = {format_amount(slab_2)}")
print(f"201 - 300 Per Unit ₹8 = {format_amount(slab_3)}")
print(f"301 - Above Per Unit ₹10 = {format_amount(slab_4)}")
print()
print(f"Electricity Charge : ₹{format_amount(electricity_charge)}")
print(f"Fixed Charge : ₹{format_amount(fixed_charge)}")
print(f"Tax (10%) : ₹{format_amount(tax)}")
print(f"Total Bill : ₹{format_amount(total_bill)}")
