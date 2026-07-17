# RESTAURANT ORDER SYSTEM
# Author: Muhammad Abdullah Farooq
# Language: Python
# Level: Beginner

from datetime import datetime
import sys
import os
import json

print ("============ Welcome to Restaurant Order System =============")

# ---------------- RESTAURANT ORDER SYSTEM ----------------  

def load_menu():
    if os.path.exists("menu.json"):
        with open("menu.json", "r") as file:
            data = json.load(file)
        return data
    else:
        return []

def save_menu(menu_data=None):
    if menu_data is None:
        menu_data = menu
    with open("menu.json", "w") as file:
        json.dump(menu_data, file, indent=5)

menu = load_menu()

if not menu:
    menu = [
        {"Item ID":101,"Name":"Zinger Burger","Category":"Burger","Price":650,"Stock":20},
        {"Item ID":102,"Name":"Beef Burger","Category":"Burger","Price":750,"Stock":18},
        {"Item ID":103,"Name":"Chicken Shawarma","Category":"Wrap","Price":450,"Stock":25},
        {"Item ID":104,"Name":"Pizza Slice","Category":"Pizza","Price":300,"Stock":30},
        {"Item ID":105,"Name":"Small Pizza","Category":"Pizza","Price":1200,"Stock":10},
        {"Item ID":106,"Name":"Large Pizza","Category":"Pizza","Price":2200,"Stock":8},
        {"Item ID":107,"Name":"Chicken Biryani","Category":"Rice","Price":400,"Stock":25},
        {"Item ID":108,"Name":"Beef Biryani","Category":"Rice","Price":500,"Stock":18},
        {"Item ID":109,"Name":"Chicken Karahi","Category":"Desi","Price":1800,"Stock":10},
        {"Item ID":110,"Name":"Beef Karahi","Category":"Desi","Price":2200,"Stock":8},
        {"Item ID":111,"Name":"French Fries","Category":"Sides","Price":250,"Stock":40},
        {"Item ID":112,"Name":"Chicken Nuggets","Category":"Sides","Price":550,"Stock":25},
        {"Item ID":113,"Name":"Cold Drink","Category":"Beverage","Price":120,"Stock":60},
        {"Item ID":114,"Name":"Mineral Water","Category":"Beverage","Price":80,"Stock":70},
        {"Item ID":115,"Name":"Coffee","Category":"Hot Drink","Price":250,"Stock":25},
        {"Item ID":116,"Name":"Tea","Category":"Hot Drink","Price":120,"Stock":35},
        {"Item ID":117,"Name":"Ice Cream","Category":"Dessert","Price":300,"Stock":20},
        {"Item ID":118,"Name":"Chocolate Cake","Category":"Dessert","Price":350,"Stock":15},
        {"Item ID":119,"Name":"Pasta","Category":"Italian","Price":850,"Stock":15},
        {"Item ID":120,"Name":"Lasagna","Category":"Italian","Price":950,"Stock":10},
        {"Item ID":121,"Name":"Club Sandwich","Category":"Sandwich","Price":550,"Stock":18},
        {"Item ID":122,"Name":"Chicken Roll","Category":"Roll","Price":280,"Stock":30},
        {"Item ID":123,"Name":"Chicken Tikka","Category":"BBQ","Price":550,"Stock":20},
        {"Item ID":124,"Name":"Seekh Kebab","Category":"BBQ","Price":450,"Stock":20},
        {"Item ID":125,"Name":"Falooda","Category":"Dessert","Price":320,"Stock":15}
    ]
    save_menu(menu)

# ---------------- FILE HANDLING ----------------
def load_order():
    if os.path.exists("order.json"):
        with open("order.json", "r") as file:
            data = json.load(file)
        return data
    else:
        return []


def load_order_history():
    if os.path.exists("order_history.json"):
        with open("order_history.json", "r") as file:
            data = json.load(file)
        return data
    else:
        return []


order = load_order()
order_history = load_order_history()


def save_order(order_data=None):
    if order_data is None:
        order_data = order
    with open("order.json", "w") as file:
        json.dump(order_data, file, indent=5)


def save_order_history(order_history_data=None):
    if order_history_data is None:
        order_history_data = order_history
    with open("order_history.json", "w") as file:
        json.dump(order_history_data, file, indent=5)


if not order:
    order = []
    save_order()

# ------------------- FUNCTIONS -----------------

def format_currency(amount):
    return f"Rs. {amount}"

def view_menu():
    if len(menu) == 0:
        print("No Items in stock!")
        return

    print("========== RESTAURANT MENU ========== ")
    sorted_menu = sorted(menu, key=lambda item: (item["Category"].lower(), item["Name"].lower()))
    current_category = None

    for item in sorted_menu:
        if item["Category"] != current_category:
            current_category = item["Category"]
            print()
            print(f"===================== {current_category.upper()} =====================")
            print("{:<6} {:<22} {:>12} {:>8}".format("ID", "Name", "Price", "Stock"))
            print("------------------------------------------------------")

        print("{:<6} {:<22} {:>12} {:>8}".format(
            item["Item ID"],
            item["Name"],
            format_currency(item["Price"]),
            item["Stock"],
        ))

def search_food_item():
    print("Search by:\n1. Item ID\n2. Name\n3. Category")
    search_choice = input("Enter your choice: ").strip()

    if search_choice == "1":
        try:
            search_id = int(input("Enter the Item ID: "))
        except ValueError:
            print("Invalid Item ID! Please enter a number.")
            return

        if search_id <= 0:
            print("Enter a valid Item ID!")
            return

        found_item = next((item for item in menu if item["Item ID"] == search_id), None)
        if found_item:
            print("---------------------------------------------------")
            print("Name:", found_item["Name"])
            print("Category:", found_item["Category"])
            print("Item ID:", found_item["Item ID"])
            print("Price:", format_currency(found_item["Price"]))
            print("Stock:", found_item["Stock"])
            print("---------------------------------------------------")
            return

        print("Item ID not found in menu.")
        return

    if search_choice == "2":
        search_name = input("Enter the item name to search: ").strip().lower()
        if not search_name:
            print("Please enter a valid name.")
            return

        results = [item for item in menu if search_name in item["Name"].lower()]
        if not results:
            print("No items found with that name.")
            return

        print("{:<6} {:<22} {:<12} {:>12} {:>8}".format("ID", "Name", "Category", "Price", "Stock"))
        print("==========================================================")
        for item in results:
            print("{:<6} {:<22} {:<12} {:>12} {:>8}".format(
                item["Item ID"],
                item["Name"],
                item["Category"],
                format_currency(item["Price"]),
                item["Stock"],
            ))
        return

    if search_choice == "3":
        search_category = input("Enter the category to search: ").strip().lower()
        if not search_category:
            print("Please enter a valid category.")
            return

        results = [item for item in menu if search_category in item["Category"].lower()]
        if not results:
            print("No items found in that category.")
            return

        print("{:<6} {:<22} {:<12} {:>12} {:>8}".format("ID", "Name", "Category", "Price", "Stock"))
        print("==========================================================")
        for item in results:
            print("{:<6} {:<22} {:<12} {:>12} {:>8}".format(
                item["Item ID"],
                item["Name"],
                item["Category"],
                format_currency(item["Price"]),
                item["Stock"],
            ))
        return

    print("Invalid search choice. Please select 1, 2, or 3.")

def place_order():
    global order

    try:
        item_id = int(input("Enter the Item ID: "))
    except ValueError:
        print("Invalid Item ID! Please enter a number.")
        return

    if item_id <= 0:
        print("Enter a valid Item ID!")
        return

    item = next((i for i in menu if i["Item ID"] == item_id), None)
    if item is None:
        print("Item not found!")
        return

    print("Selected Item:")
    print("Name :", item["Name"])
    print("Price :", format_currency(item["Price"]))
    print("Available Stock :", item["Stock"])

    try:
        quantity = int(input("Enter the quantity: "))
        if quantity <= 0:
            print("Quantity must be a positive number!")
            return
    except ValueError:
        print("Invalid quantity! Please enter a number.")
        return

    if item["Stock"] < quantity:
        print("Not enough stock available!")
        return

    item["Stock"] -= quantity

    existing_order_item = next((o for o in order if o["Item ID"] == item_id), None)
    if existing_order_item:
        existing_order_item["Quantity"] += quantity
    else:
        order.append({
            "Item ID": item_id,
            "Name": item["Name"],
            "Category": item["Category"],
            "Price": item["Price"],
            "Quantity": quantity,
        })
    save_order()
    save_menu()
    print(f"{quantity} x {item['Name']} added successfully. Remaining Stock: {item['Stock']}")

def view_current_order():
    if not order:
        print("Order is Empty!")
        return
    print("--------------------------- Current Order Details --------------------------")
    print("-----------------------------------------------------------------------------")
    print("{:<6} {:<20} {:>12} {:>15} {:>15}".format("ID", "Name", "Price", "Quantity", "Total"))
    print("-----------------------------------------------------------------------------")
    for item in order:
        subtotal = item["Price"] * item["Quantity"]
        print("{:<6} {:<20} {:>12} {:>15} {:>15}".format(
            item["Item ID"],
            item["Name"],
            format_currency(item["Price"]),
            item["Quantity"],
            format_currency(subtotal),
        ))
    print("-----------------------------------------------------------------------------")

def update_order():
    if not order:
        print("Order is Empty! Nothing to update.")
        return

    try:
        item_id = int(input("Enter the Item ID to update: "))
    except ValueError:
        print("Invalid Item ID! Please enter a number.")
        return

    order_item = next((o for o in order if o["Item ID"] == item_id), None)
    if order_item is None:
        print("Item not found in current order.")
        return

    menu_item = next((m for m in menu if m["Item ID"] == item_id), None)
    if menu_item is None:
        print("Menu item not found. Data mismatch.")
        return

    print("Current quantity:", order_item["Quantity"])
    try:
        new_quantity = int(input("Enter the new quantity: "))
    except ValueError:
        print("Invalid quantity! Please enter a number.")
        return

    if new_quantity <= 0:
        print("Quantity must be greater than 0!")
        return

    old_quantity = order_item["Quantity"]
    quantity_diff = new_quantity - old_quantity

    if quantity_diff > 0:
        if menu_item["Stock"] < quantity_diff:
            print("Not enough stock available!")
            return
        menu_item["Stock"] -= quantity_diff
    elif quantity_diff < 0:
        menu_item["Stock"] += abs(quantity_diff)

    order_item["Quantity"] = new_quantity
    save_menu()
    save_order()
    print("Order updated successfully!")

def remove_item_from_order():
    if not order:
        print("Order is Empty! Nothing to remove.")
        return

    try:
        item_id = int(input("Enter the Item ID to remove: "))
    except ValueError:
        print("Invalid Item ID! Please enter a number.")
        return

    order_item = next((o for o in order if o["Item ID"] == item_id), None)
    if order_item is None:
        print("Item not found in current order.")
        return

    print("Removing:", order_item["Name"], "x", order_item["Quantity"])
    confirm = input("Are you sure you want to remove this item? (y/n): ").strip().lower()
    if confirm != "y":
        print("Removal cancelled.")
        return

    menu_item = next((m for m in menu if m["Item ID"] == item_id), None)
    if menu_item:
        menu_item["Stock"] += order_item["Quantity"]

    order.remove(order_item)
    save_order()
    save_menu()
    print("Item removed from order successfully.")

def calculate_bill():
    if not order:
        print("Order is Empty! No bill available.")
        return 0

    grand_total = 0
    print("====================== BILL ======================")
    for index, item in enumerate(order, start=1):
        subtotal = item["Price"] * item["Quantity"]
        grand_total += subtotal
        print("{:<4} {:<17} {:>3} × {:>2} = {:>12}".format(
            f"{index:02d}.",
            item["Name"][:17],
            format_currency(item["Price"]),
            item["Quantity"],
            format_currency(subtotal),
        ))

    print("-----------------------------------------------------")
    print("{:<25} {:>12}".format("Grand Total", format_currency(grand_total)))
    print("=====================================================")
    return grand_total

def get_next_receipt_number():
    receipt_files = [name for name in os.listdir(".") if name.startswith("receipt_") and name.endswith(".txt")]
    receipt_numbers = []
    for filename in receipt_files:
        try:
            receipt_numbers.append(int(filename[len("receipt_"):-4]))
        except ValueError:
            continue
    if receipt_numbers:
        return max(receipt_numbers) + 1
    return 1001

def checkout():
    if not order:
        print("Order is Empty! Cannot proceed to checkout.")
        return

    grand_total = calculate_bill()

    name = input("Enter customer name (leave blank for 'Guest'): ").strip() or "Guest"
    phone = input("Enter customer phone (optional): ").strip()

    confirm = input(f"Proceed to checkout and generate bill for {name}? (y/n): ")
    if confirm.lower() != 'y':
        print("Checkout cancelled.")
        return

    now = datetime.now()
    receipt_number = get_next_receipt_number()
    receipt_file = f"receipt_{receipt_number}.txt"

    lines = []
    lines.append("="*60)
    lines.append("{:^60}".format("Food Order - RECEIPT"))
    lines.append("="*60)
    lines.append(f"Receipt No: {receipt_number}")
    lines.append(f"Customer: {name}")
    if phone:
        lines.append(f"Phone   : {phone}")
    lines.append(f"Date and Time   : {now.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("-"*60)
    lines.append("{:<6} {:<20} {:>7} {:>12}".format("ID", "Name", "Qty", "Subtotal"))
    lines.append("-"*60)

    for item in order:
        subtotal = item["Price"] * item["Quantity"]
        lines.append("{:<6} {:<20} {:>6} {:>12}".format(
            item["Item ID"],
            item["Name"][:25],
            item["Quantity"],
            format_currency(subtotal),
        ))
        lines.append(f"   {item['Name'][:25]} {format_currency(item['Price'])} × {item['Quantity']} = {format_currency(subtotal)}")

    lines.append("-"*60)
    lines.append(f"{'Grand Total:':>26} {format_currency(grand_total)}")
    lines.append("="*60)

    bill_text = "\n".join(lines)

    with open(receipt_file, "w", encoding="utf-8") as file:
        file.write(bill_text)

    print(f"\n{bill_text}\n")
    print(f"Receipt saved to {receipt_file}")

    order_history.append({
        "Receipt No": receipt_number,
        "Customer Name": name,
        "Phone": phone,
        "Date": now.strftime("%Y-%m-%d"),
        "Time": now.strftime("%H:%M:%S"),
        "Items": [
            {
                "Item ID": item["Item ID"],
                "Name": item["Name"],
                "Price": item["Price"],
                "Quantity": item["Quantity"],
                "Subtotal": item["Price"] * item["Quantity"],
            }
            for item in order
        ],
        "Grand Total": grand_total,
    })
    save_order_history()

    order.clear()
    save_order()
    save_menu()
    print("Thank you for ordering with us!")

def exit_system():
    print("Thank you for ordering with us!")
    print("Good Bye! Have a nice day!")
    print("Exiting the Resturant Order System...")
    input("Press Enter to close window!")
    sys.exit()

while True:
    print()
    print("=============== Select the Option (0-8) ===============")
    print("1. View Menu")
    print("2. Search Food Item")
    print("3. Place Order")
    print("4. View Current Order")
    print("5. Update Order")
    print("6. Remove Item from Order")
    print("7. Calculate Bill")
    print("8. Checkout")
    print("0. Exit")
    print("========================================================")


    try:
        choice = int(input("Enter the number: "))
    except ValueError:
        print("Invalid Choice! Please enter a number.")
        continue
    except Exception as e:
        print(f"An error occurred: {e}")
        continue

    print()
    print()
    
    if choice == 1:
        view_menu()
    elif choice == 2:
        search_food_item()
    elif choice == 3:
        place_order()
    elif choice == 4:
        view_current_order()
    elif choice == 5:
        update_order()
    elif choice == 6:
        remove_item_from_order()
    elif choice == 7:
        calculate_bill()
    elif choice == 8:
        checkout()
    elif choice == 0:
        exit_system()
    else:
        print("Invalid choice! Please try again.")
