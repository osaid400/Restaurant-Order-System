# ==========================================
# RESTAURANT ORDER SYSTEM
# Author: Muhammad Abdullah Farooq
# Language: Python 3
# ==========================================

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

def admin_login():
    admin_username = "admin"
    admin_password = "12345"

    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if username == admin_username and password == admin_password:
        print("Admin login successful!")
        return True
    else:
        print("Invalid credentials! Access denied.")
        return False

def admin_menu():

    while True:
        print("===================== ADMIN MENU ======================")
        print("=============== Select the Option (0-8) ===============")
        print("1. View Menu")
        print("2. Add New Item")
        print("3. Update Item")
        print("4. Remove Item")
        print("5. View Order History")
        print("6. View Sales Report")
        print("0. Exit Admin Menu")
        print("=========================================================")

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
            add_new_item()
        elif choice == 3:
            update_item()
        elif choice == 4:
            remove_item()
        elif choice == 5:
            view_order_history()
        elif choice == 6:
            view_sales_report()
        elif choice == 0:
            print("Exiting Admin Menu...")
            return

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

def add_new_item():
    try:
        item_id = int(input("Enter the Item ID: "))
    except ValueError:
        print("Invalid Item ID! Please enter a number.")
        return

    if item_id <= 0:
        print("Enter a valid Item ID!")
        return

    if any(item["Item ID"] == item_id for item in menu):
        print("Item ID already exists! Please use a unique Item ID.")
        return

    name = input("Enter the item name: ").strip()
    if not name:
        print("Item name cannot be empty!")
        return

    category = input("Enter the category: ").strip()
    if not category:
        print("Category cannot be empty!")
        return

    try:
        price = float(input("Enter the price: "))
    except ValueError:
        print("Invalid price! Please enter a number.")
        return

    if price <= 0:
        print("Price must be greater than 0!")
        return

    try:
        stock = int(input("Enter the stock quantity: "))
    except ValueError:
        print("Invalid stock quantity! Please enter a number.")
        return

    if stock < 0:
        print("Stock quantity cannot be negative!")
        return

    new_item = {
        "Item ID": item_id,
        "Name": name,
        "Category": category,
        "Price": price,
        "Stock": stock,
    }
    menu.append(new_item)
    save_menu()
    print(f"Item '{name}' added successfully!")

def update_item():
    try:
        item_id = int(input("Enter the Item ID to update: "))
    except ValueError:
        print("Invalid Item ID! Please enter a number.")
        return

    item = next((i for i in menu if i["Item ID"] == item_id), None)
    if item is None:
        print("Item not found!")
        return

    print("Current Item Details:")
    print(f"Name: {item['Name']}")
    print(f"Category: {item['Category']}")
    print(f"Price: {format_currency(item['Price'])}")
    print(f"Stock: {item['Stock']}")

    name = input("Enter the new name (leave blank to keep current): ").strip()
    category = input("Enter the new category (leave blank to keep current): ").strip()
    
    price_input = input("Enter the new price (leave blank to keep current): ").strip()
    stock_input = input("Enter the new stock quantity (leave blank to keep current): ").strip()

    if name:
        item["Name"] = name
    if category:
        item["Category"] = category
    if price_input:
        try:
            price = float(price_input)
            if price <= 0:
                print("Price must be greater than 0! Keeping current price.")
            else:
                item["Price"] = price
        except ValueError:
            print("Invalid price! Keeping current price.")
    if stock_input:
        try:
            stock = int(stock_input)
            if stock < 0:
                print("Stock quantity cannot be negative! Keeping current stock.")
            else:
                item["Stock"] = stock
        except ValueError:
            print("Invalid stock quantity! Keeping current stock.")

    save_menu()
    print(f"Item '{item['Name']}' updated successfully!")

def remove_item():
    try:
        item_id = int(input("Enter the Item ID to remove: "))
    except ValueError:
        print("Invalid Item ID! Please enter a number.")
        return

    item = next((i for i in menu if i["Item ID"] == item_id), None)
    if item is None:
        print("Item not found!")
        return

    confirm = input(f"Are you sure you want to remove '{item['Name']}'? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Removal cancelled.")
        return

    menu.remove(item)
    save_menu()
    print(f"Item '{item['Name']}' removed successfully!")

def top_selling_items(): 
    if not order_history:
        print("No sales data available.")
        return

    item_sales = {}
    for order_record in order_history:
        for item in order_record["Items"]:
            item_id = item["Item ID"]
            quantity = item["Quantity"]
            if item_id in item_sales:
                item_sales[item_id]["Quantity"] += quantity
            else:
                item_sales[item_id] = {
                    "Name": item["Name"],
                    "Quantity": quantity
                }

    top_items = sorted(item_sales.items(), key=lambda x: x[1]["Quantity"], reverse=True)[:5]

    print("==================== TOP SELLING ITEMS ====================")
    print("{:<6} {:<22} {:>12}".format("ID", "Name", "Total Sold"))
    print("===========================================================")
    for item_id, data in top_items:
        print("{:<6} {:<22} {:>12}".format(item_id, data["Name"], data["Quantity"]))
    print("===========================================================")

def search_by_price_range():
    try:
        min_price = float(input("Enter minimum price: "))
        max_price = float(input("Enter maximum price: "))
    except ValueError:
        print("Invalid input! Please enter valid numbers for price range.")
        return

    if min_price < 0 or max_price < 0 or min_price > max_price:
        print("Invalid price range! Please ensure min price is less than or equal to max price and both are non-negative.")
        return

    results = [item for item in menu if min_price <= item["Price"] <= max_price]

    if not results:
        print(f"No items found in the price range Rs. {min_price} - Rs. {max_price}.")
        return

    print(f"Items in the price range Rs. {min_price} - Rs. {max_price}:")
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

def view_order_history():
    if not order_history:
        print("No order history available.")
        return

    print("==================== ORDER HISTORY ====================")
    for order_record in order_history:
        print(f"Receipt No: {order_record['Receipt No']}, Customer: {order_record['Customer Name']}, Date: {order_record['Date']}, Time: {order_record['Time']}, Total: {format_currency(order_record['Grand Total'])}, Payment Method: {order_record['Payment Method']}")
    print("=======================================================")

def view_sales_report():
    if not order_history:
        print("==================== SALES REPORT ====================")
        print("No sales data available.")
        print("=======================================================")
        return

    total_sales = sum(order_record['Grand Total'] for order_record in order_history)
    total_orders = len(order_history)

    print("==================== SALES REPORT ====================")
    print(f"Total Orders: {total_orders}")
    print(f"Total Sales: {format_currency(total_sales)}")
    print("=======================================================")

def search_food_item():
    print("Search by:\n1. Item ID\n2. Name\n3. Category \n 4. Seach by Price Range")
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

    if search_choice == "4":
        search_by_price_range()
        return

    print("Invalid search choice. Please select 1, 2, 3, or 4.")

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

def apply_discount(grand_total):
    if grand_total >= 5000:
        discount = 0.10
    elif grand_total >= 3000:
        discount = 0.05
    else:
        discount = 0.0

    discounted_total = grand_total * (1 - discount)
    return discounted_total, discount

def choose_order_type():
    print("==================== ORDER TYPE ====================")
    print("Choose Order Type:")
    print("1. Dine-In")
    print("2. Takeaway")
    print("=====================================================")

    order_type_choice = input("Enter your choice (1 or 2): ").strip()

    if order_type_choice == "1":
        try:
            table_number = input("Table Number (1 to 10): ").strip()
            table_number = int(table_number)
            if table_number < 1 or table_number > 10:
                print("Invalid table number! Please enter a number between 1 and 10.")
                return "Dine-In", None
        except ValueError:
            print("Invalid table number! Please enter a valid number.")
            return "Dine-In", None

        return "Dine-In", table_number
    
    elif order_type_choice == "2":
        return "Takeaway", None
    else:
        print("Invalid choice! Defaulting to 'Dine-In'.")
        return "Dine-In", None

def calculate_GST(grand_total):
    gst_rate = 0.17
    gst_amount = grand_total * gst_rate
    total_with_gst = grand_total + gst_amount
    return total_with_gst, gst_amount

def final_bill():
    if not order:
        print("======================================")
        print("Order is Empty! Cannot calculate bill.")
        print("======================================")
        return 0

    grand_total = sum(item["Price"] * item["Quantity"] for item in order)
    discounted_total, discount_rate = apply_discount(grand_total)
    total_with_gst, gst_amount = calculate_GST(discounted_total)

    print("\n==================== FINAL BILL ====================")
    print("{:<6} {:<20} {:>12} {:>15} {:>15}".format("ID", "Name", "Price", "Quantity", "Total"))
    print("-----------------------------------------------------")
    for item in order:
        subtotal = item["Price"] * item["Quantity"]
        print("{:<6} {:<20} {:>12} {:>15} {:>15}".format(
            item["Item ID"],
            item["Name"],
            format_currency(item["Price"]),
            item["Quantity"],
            format_currency(subtotal),
        ))
    print("-----------------------------------------------------")
    print(f"{'Grand Total:':>54} {format_currency(grand_total)}")
    if discount_rate > 0:
        print(f"{'Discount Applied:':>54} {discount_rate*100:.0f}%")
        print(f"{'Total after Discount:':>54} {format_currency(discounted_total)}")
    print(f"{'GST (17%):':>54} {format_currency(gst_amount)}")
    print(f"{'Total Payable:':>54} {format_currency(total_with_gst)}")
    print("=====================================================")

    return total_with_gst

def payment_method():
    print("==================== PAYMENT METHOD ====================")
    print("Choose Payment Method:")
    print("1. Cash")
    print("2. Card")
    print("3. Mobile Payment")
    print("=========================================================")

    payment_choice = input("Enter your choice (1, 2, or 3): ").strip()

    if payment_choice == "1":
        return "Cash"
    elif payment_choice == "2":
        return "Card"
    elif payment_choice == "3":
        return "Mobile Payment"
    else:
        print("Invalid choice! Defaulting to 'Cash'.")
        return "Cash"

def get_next_receipt_number():
    if not os.path.exists("customer_receipts"):
        os.makedirs("customer_receipts")
    
    receipt_files = [name for name in os.listdir("customer_receipts") if name.startswith("receipt_") and name.endswith(".txt")]
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

    grand_total = final_bill()

    name = input("Enter customer name (leave blank for 'Guest'): ").strip() or "Guest"
    phone = input("Enter customer phone (optional): ").strip()
    payment_type = payment_method()

    confirm = input(f"Proceed to checkout and generate bill for {name}? (y/n): ")
    if confirm.lower() != 'y':
        print("Checkout cancelled.")
        return

    now = datetime.now()
    receipt_number = get_next_receipt_number()
    receipt_file = os.path.join("customer_receipts", f"receipt_{receipt_number}.txt")

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
    lines.append(f"{'Payment Method:':>26} {payment_type}")
    lines.append("="*60)

    bill_text = "\n".join(lines)

    # Ensure folder exists before saving
    if not os.path.exists("customer_receipts"):
        os.makedirs("customer_receipts")
    
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
        "Payment Method": payment_type,
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
        "Payment Method": payment_type,
    })
    save_order_history()

    order.clear()
    save_order()
    save_menu()
    print("Thank you for ordering with us!")

def exit_system():
    print("Thank you for ordering with us!")
    print("Good Bye! Have a nice day!")
    print("Exiting the Restaurant Order System...")
    input("Press Enter to close window!")
    sys.exit()

def customer_menu():

    while True:
        print("=============== Welcome to the Restaurant Order System ===============")
        print("Please select an option from the menu below:")
        print("1. View Menu")
        print("2. Search Food Item")
        print("3. Place Order")
        print("4. View Current Order")
        print("5. Update Order")
        print("6. Remove Item from Order")
        print("7. Calculate Bill")
        print("8. Checkout")
        print("0. Exit as Customer")
        print("======================================================================")

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
            final_bill()
        elif choice == 8:
            checkout()
        elif choice == 0:
            main_menu()
        else:
            print("Invalid choice! Please try again.")

def main_menu():
    while True:
        print("==================== MAIN MENU ====================")
        print("1. Admin Login")
        print("2. Customer Menu")
        print("0. Exit")
        print("===================================================")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid Choice! Please enter a number.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

        if choice == 1:
            if admin_login():
                admin_menu()
        elif choice == 2:
            customer_menu()
        elif choice == 0:
            exit_system()
        else:
            print("Invalid choice! Please try again.")

main_menu()