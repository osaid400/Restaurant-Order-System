# Restaurant Order System

A simple console-based **Restaurant Order System** built with Python. This project demonstrates the use of functions, lists, dictionaries, loops, searching, and input validation to simulate a restaurant ordering system.

---

## Features

* View restaurant menu grouped by category
* Search food items by:
  * Item ID
  * Item Name
  * Category
* Place food orders
* Update order quantity
* Remove items from an order
* Calculate total bill
* Checkout with receipt generation
* Automatic stock management
* Input validation for all user entries

---

## Technologies Used

* Python 3

---

## Concepts Covered

* Functions
* Lists
* Dictionaries
* Loops
* Conditional Statements
* User Input Validation
* Searching
* Sorting (`sorted()`)
* List Comprehensions
* `next()` Function
* String Formatting
* Console-Based Application Design

---

## Project Structure

```text
Restaurant-Order-System/
│
├── Restaurant Order System.py
└── README.md
```

---

## How to Run

1. Clone the repository

```bash
git clone https://github.com/osaid400/Restaurant-Order-System.git
```

2. Open the project folder

```bash
cd Restaurant-Order-System
```

3. Run the application

```bash
python "Restaurant Order System.py"
```

---

# Example Output

## Main Menu

```text
============ Welcome to Restaurant Order System ============

=============== Select the Option (0-8) ===============
1. View Menu
2. Search Food Item
3. Place Order
4. View Current Order
5. Update Order
6. Remove Item from Order
7. Calculate Bill
8. Checkout
0. Exit
========================================================
```

---

## View Menu

```text
===================== BURGER =====================

ID     Name                     Price        Stock
------------------------------------------------------
101    Zinger Burger            Rs. 650      20
102    Beef Burger              Rs. 750      18
```

---

## Place Order

```text
Enter the Item ID: 101

Selected Item:
Name : Zinger Burger
Price : Rs. 650
Available Stock : 20

Enter the quantity: 2

2 x Zinger Burger added successfully.
Remaining Stock: 18
```

---

## Current Order

```text
ID     Name                 Price      Quantity      Total
--------------------------------------------------------------
101    Zinger Burger        Rs. 650          2     Rs. 1300
--------------------------------------------------------------
```

---

## Bill

```text
====================== BILL ======================

01. Zinger Burger      x2      Rs. 1300

-------------------------------------------------
Grand Total             Rs. 1300
=================================================
```

---

## Checkout

```text
Proceed to Checkout? (Y/N): y

========= RECEIPT =========

01. Zinger Burger      x2      Rs. 1300

------------------
Grand Total
Rs. 1300

Thank you!
============================
```

---

## Future Improvements

* Store orders using file handling
* Save customer information
* Generate invoice numbers
* Apply discounts and coupons
* Add GST/Tax calculation
* Add multiple payment methods
* Store order history
* Admin panel for menu management
* Database integration (SQLite/MySQL)
* Graphical User Interface (Tkinter/PyQt)

---

## Learning Outcomes

This project helped me practice:

* Designing menu-driven applications
* Managing inventory using dictionaries
* Working with lists of records
* Searching and sorting data
* Updating and deleting records
* Handling user input safely
* Writing modular code using functions
* Building a complete CRUD-style console application

---

## Author

**Muhammad Abdullah Farooq**

GitHub: https://github.com/osaid400
