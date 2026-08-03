
# Restaurant Order System

A console-based Restaurant Order System built with Python using Object-Oriented Programming (OOP) principles. This project demonstrates JSON file handling, stock management, receipt generation, order history, user/admin authentication, and menu-driven programming.

---

## Features

* Object-Oriented Design (OOP with `MenuItem`, `OrderItem`, `User`, and `RestaurantManager` classes)
* Admin & Customer Dual-Panel System
* Menu Management (Add, Update, Remove, View Items)
* Search Food Item
  * By Item ID
  * By Name
  * By Category
  * By Price Range
* Place Order & Real-Time Stock Updates
* View Current Order
* Update Order Quantity
* Remove Item From Order
* Calculate Bill (Auto Discount & 5% GST Calculation)
* Order Type Selection (Dine-In with Table Number / Takeaway)
* Payment Method Options (Cash / Card / Mobile Payment)
* Checkout System & Sales Reporting
* Automatic Receipt Number Generation
* Save Customer Receipts (.txt)
* User Authentication & Admin Security Persistence (`users.json`)
* Menu & Order Persistence (`menu.json`, `order.json`, `order_history.json`)
* Input Validation & Robust Exception Handling

---

## Technologies Used

* Python 3 
* JSON (Data Persistence)
* Datetime Module
* OS & Sys Modules

---

## Project Structure

```text
Restaurant-Order-System/
│
├── restaurant_order_system.py
├── menu.json
├── customer_receipts/
│   ├── receipt_1001.txt
│   └── ...
├── .gitignore
└── README.md

```

---

## How to Run

Clone the repository

```bash
git clone (https://github.com/osaid400/Restaurant-Order-System.git)

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

### Main Menu & Admin Login

```text
=============== Welcome to the Restaurant Order System ===============
1. Order as Customer
2. Login as Admin
0. Exit
======================================================================
Enter your choice (1, 2, or 0): 2
Enter admin username: admin
Enter admin password: 12345
Admin login successful!

===================== ADMIN MENU ======================
1. View Menu
2. Add New Item
3. Update Item
4. Remove Item
5. View Order History
6. View Sales Report
0. Exit Admin Menu
=========================================================

```

---

### View Menu

```text
========================= RESTAURANT MENU =========================

---------------------------- BURGER -----------------------------
ID       Name                            Price    Stock
--------------------------------------------------------------
101      Zinger Burger               Rs. 650.00       20
102      Beef Burger                 Rs. 750.00       18

---------------------------- PIZZA -----------------------------
ID       Name                            Price    Stock
--------------------------------------------------------------
105      Small Pizza                Rs. 1200.00       10
106      Large Pizza                Rs. 2200.00        8
==================================================================

```

---

### Search Food Item

```text
Search by:
1. Item ID
2. Name
3. Category
4. Search by Price Range
Enter your choice: 2
Enter the item name to search: pizza

ID       Name                   Category             Price    Stock
====================================================================
105      Small Pizza            Pizza          Rs. 1200.00       10
106      Large Pizza            Pizza          Rs. 2200.00        8

```

---

### Place Order

```text
Enter the Item ID: 105

Selected Item:
Name            : Small Pizza
Price           : Rs. 1200.00
Available Stock : 10
Enter the quantity: 2

2 x Small Pizza added successfully. Remaining Stock: 8

```

---

### View Current Order

```text
============================ CURRENT ORDER ==========================
ID       Name                         Price      Qty     Subtotal
----------------------------------------------------------------------
105      Small Pizza            Rs. 1200.00        2  Rs. 2400.00
----------------------------------------------------------------------
                                       Current Total: Rs. 2400.00
======================================================================

```

---

### Update Order

```text
Current quantity: 2
Enter the new quantity: 3
Order updated successfully!

```

---

### Remove Item from Order

```text
Enter the Item ID to remove: 105
Item removed from order successfully.

```

---

### Calculate Bill

```text
=============================== FINAL BILL ===============================
ID       Name                            Price      Qty          Total
---------------------------------------------------------------------------
105      Small Pizza               Rs. 1200.00        2    Rs. 2400.00
113      Cold Drink                 Rs. 120.00        2     Rs. 240.00
---------------------------------------------------------------------------
                                             Subtotal: Rs.    2640.00
                                             GST (5%): Rs.     132.00
==========================================================================
                                        Total Payable: Rs.    2772.00
==========================================================================

```

---

### Checkout

```text
==================== ORDER TYPE ====================
1. Dine-In
2. Takeaway
====================================================
Enter your choice (1 or 2): 1
Table Number (1 to 10): 3

Enter customer name (leave blank for 'Guest'): Abdullah
Enter customer phone (optional): 03001234567

==================== PAYMENT METHOD ====================
1. Cash
2. Card
3. Mobile Payment
========================================================
Enter your choice (1, 2, or 3): 1

Proceed to checkout and generate bill for Abdullah? (y/n): y

============================================================
                     RESTAURANT RECEIPT                     
============================================================
Receipt No    : 1001
Customer      : Abdullah
Phone         : 03001234567
Order Type    : Dine-In (Table 3)
Date & Time   : 2026-08-03 14:30:15
------------------------------------------------------------
ID     Name                     Qty           Subtotal
------------------------------------------------------------
105    Small Pizza                2        Rs. 2400.00
113    Cold Drink                 2         Rs. 240.00
------------------------------------------------------------
                         Total Payable: Rs. 2772.00
                        Payment Method: Cash
============================================================

Receipt saved to customer_receipts/receipt_1001.txt
Thank you for ordering with us!

```

---

### Receipt Example

```text
============================================================
                     RESTAURANT RECEIPT                     
============================================================
Receipt No    : 1001
Customer      : Abdullah
Phone         : 03001234567
Order Type    : Dine-In (Table 3)
Date & Time   : 2026-08-03 14:30:15
------------------------------------------------------------
ID     Name                     Qty           Subtotal
------------------------------------------------------------
105    Small Pizza                2        Rs. 2400.00
113    Cold Drink                 2         Rs. 240.00
------------------------------------------------------------
                         Total Payable: Rs. 2772.00
                        Payment Method: Cash
============================================================

```

---

## Concepts Covered

* Object-Oriented Programming (OOP - Classes, Encapsulation, Class Methods)
* Clean Architecture & Model-View Separation
* Lists and Dictionaries with OOP Integration
* CRUD Operations (Menu Items, Orders, Users)
* JSON File Handling & Multi-File Persistence
* Search Algorithms (ID, Name, Category, Price Range filtering)
* Menu-Driven Interactive Programming
* Robust Input Validation & Exception Handling
* Datetime & OS File Management
* Automated Text Receipt Generation
* Inventory Stock Management

---

## Future Improvements

* Customer Registration & Individual Accounts
* Advanced Discount Coupon Engine
* Table Reservation Management System
* SQLite/PostgreSQL Database Integration
* GUI Version (Tkinter / PyQt)
* Advanced Sales Dashboard Analytics

---

## Learning Outcomes

This project helped me practice:

* Object-Oriented Architecture (`MenuItem`, `OrderItem`, `User`, `RestaurantManager`)
* JSON file serialization and deserialization
* Persistent data storage across sessions
* Real-time inventory and stock control
* Automated receipt generation and receipt tracking
* Order history and sales reporting
* Modular code refactoring and bug fixing
* Problem-solving and input sanitization

---

## Author

**Muhammad Abdullah Farooq**

GitHub: https://github.com/osaid400

```
