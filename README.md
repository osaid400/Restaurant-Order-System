# Restaurant Order System

A console-based Restaurant Order System built with Python. This project demonstrates menu management, food ordering, stock management, JSON file handling, receipt generation, and order history.

## Features

* View Restaurant Menu
* Search Food Item

  * By Item ID
  * By Name
  * By Category
* Place Food Order
* View Current Order
* Update Order Quantity
* Remove Item From Order
* Calculate Bill
* Checkout System
* Receipt Generation (.txt)
* Auto Receipt Number
* Order History
* Menu & Order Persistence using JSON
* Stock Management
* Input Validation
* Exception Handling

## Technologies Used

* Python 3
* JSON
* Datetime Module
* OS Module

## Project Structure

```text
Restaurant-Order-System/
│
├── restaurant_order_system.py
├── .gitignore
├── /customer_receipts
└── README.md
```

## How to Run

1. Clone the repository

```bash
git clone https://github.com/osaid400/Restaurant-Order-System.git
```

2. Open the project folder

```bash
cd Restaurant-Order-System
```

3. Run

```bash
python restaurant_order_system.py
```

---

# Example Outputs

## View Menu

```text
===================== BURGER =====================

ID     Name                    Price     Stock
------------------------------------------------
101    Zinger Burger           Rs. 650      20
102    Beef Burger             Rs. 750      18
```

---

## Search Item

```text
Search by:
1. Item ID
2. Name
3. Category

Enter your choice: 2
Enter item name: pizza

ID     Name              Category     Price     Stock
------------------------------------------------------
105    Small Pizza       Pizza      Rs. 1200      10
106    Large Pizza       Pizza      Rs. 2200       8
```

---

## Place Order

```text
Enter Item ID: 105

Selected Item:
Name : Small Pizza
Price : Rs. 1200
Available Stock : 10

Enter Quantity: 2

2 x Small Pizza added successfully.
Remaining Stock: 8
```

---

## Current Order

```text
ID     Name                  Price      Quantity        Total
--------------------------------------------------------------
105    Small Pizza         Rs.1200          2       Rs.2400
```

---

## Update Order

```text
Current Quantity: 2

Enter New Quantity: 3

Order updated successfully!
```

---

## Remove Item

```text
Removing:
Small Pizza x 3

Are you sure? (y/n): y

Item removed successfully.
```

---

## Calculate Bill

```text
====================== BILL ======================

01. Small Pizza Rs.1200 × 2 = Rs.2400
02. Cold Drink  Rs.120 × 2  = Rs.240

--------------------------------------------------
Grand Total                 Rs.2640
==================================================
```

---

## Checkout

```text
Customer Name: Abdullah
Phone: 03001234567

Proceed? (y/n): y

Receipt saved to receipt_1001.txt

Thank you for ordering with us!
```

---

## Receipt Example

```text
Receipt No: 1001

Customer: Abdullah

Small Pizza Rs.1200 × 2 = Rs.2400
Cold Drink  Rs.120 × 2 = Rs.240

Grand Total:
Rs.2640
```

## Concepts Covered

* Functions
* Lists
* Dictionaries
* JSON File Handling
* CRUD Operations
* Searching
* Input Validation
* Exception Handling
* Datetime Module
* OS Module
* Menu Driven Programming
* Stock Management
* Receipt Generation

## Future Improvements

* Customer Login System
* Admin Panel
* Discount Coupons
* Table Reservations
* SQLite Database
* GUI Version (Tkinter)
* Order Analytics Dashboard

## Learning Outcomes

This project helped me practice:

* Working with JSON files
* Persistent data storage
* CRUD operations
* Inventory management
* Receipt generation
* Order history management
* Modular programming
* Problem-solving

## Author

**Muhammad Abdullah Farooq**

GitHub: https://github.com/osaid400
