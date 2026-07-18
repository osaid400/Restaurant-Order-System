# Restaurant Order System

A console-based Restaurant Order System built with Python. This project demonstrates JSON file handling, stock management, receipt generation, order history, and menu-driven programming.

---

## Features

* View Restaurant Menu
* Search Food Item
  * By Item ID
  * By Name
  * By Category
* Place Order
* View Current Order
* Update Order Quantity
* Remove Item From Order
* Calculate Bill
* Checkout System
* Automatic Receipt Number Generation
* Save Customer Receipts (.txt)
* Order History (JSON)
* Menu Persistence (JSON)
* Current Order Persistence (JSON)
* Stock Management
* Input Validation
* Exception Handling

---

## Technologies Used

* Python 3
* JSON
* Datetime Module
* OS Module

---

## Project Structure

```text
Restaurant-Order-System/
│
├── restaurant_order_system.py
├── customer_receipts/
│   ├── receipt_1001.txt
│   ├── receipt_1002.txt
│   └── ...
├── .gitignore
└── README.md
```

---

## How to Run

Clone the repository

```bash
git clone https://github.com/osaid400/Restaurant-Order-System.git
```

Move into the project folder

```bash
cd Restaurant-Order-System
```

Run the project

```bash
python restaurant_order_system.py
```

---

## Example Outputs

## View Menu

```text
============ RESTAURANT MENU ============

===================== BURGER =====================

ID     Name                       Price   Stock
------------------------------------------------------
101    Zinger Burger            Rs. 650      20
102    Beef Burger              Rs. 750      18
```

---

## Search Food Item

```text
Search by:
1. Item ID
2. Name
3. Category

Enter your choice: 2
Enter the item name to search: pizza

ID     Name                   Category      Price   Stock
==========================================================
105    Small Pizza            Pizza      Rs. 1200      10
106    Large Pizza            Pizza      Rs. 2200       8
```

---

## Place Order

```text
Enter the Item ID: 105

Selected Item:
Name : Small Pizza
Price : Rs. 1200
Available Stock : 10

Enter the quantity: 2

2 x Small Pizza added successfully.
Remaining Stock: 8
```

---

## View Current Order

```text
--------------------------- Current Order Details --------------------------

-----------------------------------------------------------------------------
ID     Name                     Price        Quantity          Total
-----------------------------------------------------------------------------
105    Small Pizza           Rs. 1200              2      Rs. 2400
-----------------------------------------------------------------------------
```

---

## Update Order

```text
Current quantity: 2

Enter the new quantity: 3

Order updated successfully!
```

---

## Remove Item

```text
Removing: Small Pizza x 3

Are you sure you want to remove this item? (y/n): y

Item removed from order successfully.
```

---

## Calculate Bill

```text
====================== BILL ======================

01. Small Pizza      Rs. 1200 × 2 = Rs. 2400
02. Cold Drink       Rs. 120 × 2 = Rs. 240

-----------------------------------------------------
Grand Total                  Rs. 2640
=====================================================
```

---

## Checkout

```text
Enter customer name (leave blank for 'Guest'): Abdullah
Enter customer phone (optional): 03001234567

Proceed to checkout and generate bill for Abdullah? (y/n): y

Receipt saved to customer_receipts/receipt_1001.txt

Thank you for ordering with us!
```

---

## Receipt Example

```text
============================================================
                     Food Order - RECEIPT
============================================================

Receipt No: 1001
Customer: Abdullah
Phone: 03001234567
Date and Time: 2026-07-17 19:42:15

------------------------------------------------------------

ID     Name                  Qty      Subtotal
------------------------------------------------------------
105    Small Pizza            2      Rs. 2400

113    Cold Drink             2      Rs. 240

------------------------------------------------------------
Grand Total:                 Rs. 2640
============================================================
```

---

## Concepts Covered

* Functions
* Lists
* Dictionaries
* CRUD Operations
* JSON File Handling
* Persistent Data Storage
* Search Algorithms
* Menu-Driven Programming
* Input Validation
* Exception Handling
* Datetime Module
* OS Module
* Receipt Generation
* Stock Management

---

## Future Improvements

* Admin Login
* Customer Login
* Discount Coupons
* Table Reservation
* SQLite Database
* GUI Version (Tkinter)
* Sales Reports
* Dashboard

---

## Learning Outcomes

This project helped me practice:

* JSON file handling
* Persistent data storage
* CRUD operations
* Inventory management
* Receipt generation
* Order history management
* Modular programming
* Exception handling
* Problem-solving

---

## Author

**Muhammad Abdullah Farooq**

GitHub: https://github.com/osaid400