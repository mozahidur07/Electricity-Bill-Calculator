# Electricity Bill Calculator

## Project Title

Electricity Bill Calculator

---

## Problem Statement

Write a Python program to calculate the electricity bill based on the number of units consumed.

The program will take the total electricity units from the user and calculate the bill using the slab-wise rate system. After calculating the electricity charge, it will add a fixed charge and tax to generate the final electricity bill.

---

## Objective

The objective of this project is to learn the basic concepts of Python programming such as:

- Variables
- Input and Output
- Arithmetic Operators
- Comparison Operators
- Conditional Statements (if, elif, else)

---

## Input

The program will ask the user to enter:

- Total Units Consumed

Example:

```
Enter Total Units : 450
```

---

## Slab Rate

| Units | Rate |
|-------|------|
| 1 - 100 | ₹6 per unit |
| 101 - 200 | ₹7 per unit |
| 201 - 300 | ₹8 per unit |
| Above 300 | ₹10 per unit |

---

## Additional Charges

- Fixed Charge = ₹200
- Tax = 10% of Electricity Charge

---

## Processing

The program will:

- Read total units from the user.
- Calculate the electricity charge according to slab rates.
- Add Fixed Charge.
- Calculate 10% Tax.
- Display the Final Electricity Bill.

---

## Output

Example Output

```
--------- ELECTRICITY BILL ---------

Units Consumed : 450

1 - 100 Per Unit ₹6 = 600
101 - 200 Per Unit ₹7 = 700
201 - 300 Per Unit ₹8 = 800
301 - Above Per Unit ₹10 = 1500

Electricity Charge : ₹3600
Fixed Charge : ₹200
Tax (10%) : ₹360
Total Bill : ₹4160
```

---

## Formula Used

Electricity Charge

```
Calculated according to slab rates.
```

Tax

```
Tax = Electricity Charge × 10 / 100
```

Final Bill

```
Total Bill = Electricity Charge + Fixed Charge + Tax
```

---

## Concepts Used

- Variables
- Input Function
- Output Function
- Arithmetic Operators
- Comparison Operators
- Conditional Statements (if, elif, else)

---

## Language

Python

---

## Developed By

Name : Mozahidur Rahaman

Roll No : 25103070025

Registration No. 25103003150 of 2025-2026

Department : B.Tech CSE
