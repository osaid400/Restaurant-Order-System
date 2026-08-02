# ==========================================
# RESTAURANT ORDER SYSTEM
# Author: Muhammad Abdullah Farooq
# Language: Python 3
# ==========================================

from datetime import datetime
import sys
import os
import json


class Menu_Item:

    def __init__(self, item_id, name, category, price, stock):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def to_dict(self) -> dict:
        return {
            "Item ID": self.item_id,
            "Name": self.name,
            "Category": self.category,
            "Price": self.price,
            "Stock": self.stock
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            item_id=data["Item ID"],
            name=data["Name"],
            category=data["Category"],
            price=data["Price"],
            stock=data["Stock"]
        )


class Order_Item:

    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

    def to_dict(self):
        return {
            "Menu ID": getattr(self.menu_item, 'item_id', self.menu_item),
            "Quantity": self.quantity
        }

    def subtotal(self):
        price = getattr(self.menu_item, 'price', 0)
        return price * self.quantity


class User:

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def to_dict(self):
        return {
            "Username": self.username,
            "Password": self.password,
            "Role": self.role
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            username=data["Username"],
            password=data["Password"],
            role=data["Role"]
        )


class Restaurant_Manager:

    def __init__(self, menu, order, history, users, discounts, sales, menu_file="menu.json", order_file="order.json", order_history_file="order_history.json"):
        self.menu_file = menu_file
        self.order_file = order_file
        self.order_history_file = order_history_file

        self.menu = menu
        self.order = order
        self.history = history
        self.users = users
        self.discounts = discounts
        self.sales = sales

    def _normalize_menu_item(self, item):
        if isinstance(item, dict):
            return {
                "Item ID": item.get("Item ID", item.get("item_id")),
                "Name": item.get("Name", item.get("name")),
                "Category": item.get("Category", item.get("category")),
                "Price": item.get("Price", item.get("price")),
                "Stock": item.get("Stock", item.get("stock")),
            }
        if hasattr(item, "to_dict"):
            return item.to_dict()
        return item

    def load_menu(self):
        if os.path.exists(self.menu_file):
            try:
                with open(self.menu_file, "r", encoding="utf-8") as file:
                    data = json.load(file)
                self.menu.clear()
                self.menu.extend(self._normalize_menu_item(item) for item in data if data)
            except (json.JSONDecodeError, OSError):
                self.menu.clear()
        else:
            self.menu.clear()
        return self.menu

    def save_menu(self, menu_data=None):
        data = [self._normalize_menu_item(item) for item in (self.menu if menu_data is None else menu_data)]
        with open(self.menu_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        return data

    def load_orders(self):
        if os.path.exists(self.order_file):
            try:
                with open(self.order_file, "r", encoding="utf-8") as file:
                    data = json.load(file)
                self.order.clear()
                self.order.extend(item for item in data if isinstance(item, dict))
            except (json.JSONDecodeError, OSError):
                self.order.clear()
        else:
            self.order.clear()
        return self.order

    def save_orders(self, order_data=None):
        data = list(self.order if order_data is None else order_data)
        with open(self.order_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        return data

    def load_history(self):
        if os.path.exists(self.order_history_file):
            try:
                with open(self.order_history_file, "r", encoding="utf-8") as file:
                    data = json.load(file)
                self.history.clear()
                self.history.extend(data if isinstance(data, list) else [])
            except (json.JSONDecodeError, OSError):
                self.history.clear()
        else:
            self.history.clear()
        return self.history

    def save_history(self, history_data=None):
        data = list(self.history if history_data is None else history_data)
        with open(self.order_history_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        return data

    def load_users(self):
        if os.path.exists("users.json"):
            try:
                with open("users.json", "r", encoding="utf-8") as file:
                    data = json.load(file)
                self.users.clear()
                self.users.extend(data if isinstance(data, list) else [])
            except (json.JSONDecodeError, OSError):
                self.users.clear()
        else:
            self.users.clear()
        return self.users

    def save_users(self, users_data=None):
        data = list(self.users if users_data is None else users_data)
        with open("users.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        return data

    def view_menu(self):
        if not self.menu:
            print("No Items in stock!")
            return

        print("\n========================= RESTAURANT MENU =========================")
        sorted_menu = sorted(self.menu, key=lambda item: (str(item.get("Category", "")).lower(), str(item.get("Name", "")).lower()))
        current_category = None

        for item in sorted_menu:
            category = str(item.get("Category", ""))
            if category != current_category:
                current_category = category
                print(f"\n---------------------------- {current_category.upper()} -----------------------------")
                print("{:<8} {:<28} {:>12} {:>8}".format("ID", "Name", "Price", "Stock"))
                print("-" * 62)

            print("{:<8} {:<28} {:>12} {:>8}".format(
                item.get("Item ID", ""),
                str(item.get("Name", ""))[:26],
                f"Rs. {item.get('Price', 0):.2f}",
                item.get("Stock", 0),
            ))
        print("=" * 66)

    def search_food(self):
        print("\nSearch by:\n1. Item ID\n2. Name\n3. Category\n4. Search by Price Range")
        search_choice = input("Enter your choice: ").strip()

        if search_choice == "1":
            try:
                search_id = int(input("Enter the Item ID: "))
            except ValueError:
                print("Invalid Item ID! Please enter a number.")
                return

            found_item = next((item for item in self.menu if item.get("Item ID") == search_id), None)
            if found_item:
                print("-" * 50)
                print("Name    :", found_item.get("Name"))
                print("Category:", found_item.get("Category"))
                print("Item ID :", found_item.get("Item ID"))
                print("Price   :", f"Rs. {found_item.get('Price', 0):.2f}")
                print("Stock   :", found_item.get("Stock"))
                print("-" * 50)
                return
            print("Item ID not found in menu.")
            return

        if search_choice == "2":
            search_name = input("Enter the item name to search: ").strip().lower()
            results = [item for item in self.menu if search_name in str(item.get("Name", "")).lower()]
            if not results:
                print("No items found with that name.")
                return
            print("\n{:<8} {:<22} {:<15} {:>12} {:>8}".format("ID", "Name", "Category", "Price", "Stock"))
            print("=" * 68)
            for item in results:
                print("{:<8} {:<22} {:<15} {:>12} {:>8}".format(
                    item.get("Item ID"),
                    str(item.get("Name"))[:20],
                    str(item.get("Category"))[:13],
                    f"Rs. {item.get('Price', 0):.2f}",
                    item.get("Stock"),
                ))
            return

        if search_choice == "3":
            search_category = input("Enter the category to search: ").strip().lower()
            results = [item for item in self.menu if search_category in str(item.get("Category", "")).lower()]
            if not results:
                print("No items found in that category.")
                return
            print("\n{:<8} {:<22} {:<15} {:>12} {:>8}".format("ID", "Name", "Category", "Price", "Stock"))
            print("=" * 68)
            for item in results:
                print("{:<8} {:<22} {:<15} {:>12} {:>8}".format(
                    item.get("Item ID"),
                    str(item.get("Name"))[:20],
                    str(item.get("Category"))[:13],
                    f"Rs. {item.get('Price', 0):.2f}",
                    item.get("Stock"),
                ))
            return

        if search_choice == "4":
            try:
                min_price = float(input("Enter minimum price: "))
                max_price = float(input("Enter maximum price: "))
            except ValueError:
                print("Invalid input! Please enter valid numbers for price range.")
                return
            results = [item for item in self.menu if min_price <= item.get("Price", 0) <= max_price]
            if not results:
                print(f"No items found in the price range Rs. {min_price:.2f} - Rs. {max_price:.2f}.")
                return
            print(f"\nItems in the price range Rs. {min_price:.2f} - Rs. {max_price:.2f}:")
            print("{:<8} {:<22} {:<15} {:>12} {:>8}".format("ID", "Name", "Category", "Price", "Stock"))
            print("=" * 68)
            for item in results:
                print("{:<8} {:<22} {:<15} {:>12} {:>8}".format(
                    item.get("Item ID"),
                    str(item.get("Name"))[:20],
                    str(item.get("Category"))[:13],
                    f"Rs. {item.get('Price', 0):.2f}",
                    item.get("Stock"),
                ))
            return

        print("Invalid search choice. Please select 1, 2, 3, or 4.")

    def place_order(self):
        try:
            item_id = int(input("Enter the Item ID: "))
        except ValueError:
            print("Invalid Item ID! Please enter a number.")
            return

        item = next((i for i in self.menu if i.get("Item ID") == item_id), None)
        if item is None:
            print("Item not found!")
            return

        print("\nSelected Item:")
        print("Name            :", item.get("Name"))
        print("Price           :", f"Rs. {item.get('Price', 0):.2f}")
        print("Available Stock :", item.get("Stock"))

        try:
            quantity = int(input("Enter the quantity: "))
            if quantity <= 0:
                print("Quantity must be a positive number!")
                return
        except ValueError:
            print("Invalid quantity! Please enter a number.")
            return

        if item.get("Stock", 0) < quantity:
            print("Not enough stock available!")
            return

        item["Stock"] -= quantity

        existing_order_item = next((o for o in self.order if o.get("Item ID") == item_id), None)
        if existing_order_item:
            existing_order_item["Quantity"] += quantity
        else:
            self.order.append({
                "Item ID": item_id,
                "Name": item.get("Name"),
                "Category": item.get("Category"),
                "Price": item.get("Price"),
                "Quantity": quantity,
            })
        self.save_menu()
        self.save_orders()
        print(f"\n{quantity} x {item.get('Name')} added successfully. Remaining Stock: {item.get('Stock')}")

    def view_current_order(self):
        if not self.order:
            print("\nYour current order is empty.")
            return

        print("\n==================== CURRENT ORDER ====================")
        print("{:<8} {:<24} {:>10} {:>8} {:>12}".format("ID", "Name", "Price", "Qty", "Subtotal"))
        print("-" * 66)
        total = 0
        for item in self.order:
            sub = item.get("Price", 0) * item.get("Quantity", 0)
            total += sub
            print("{:<8} {:<24} {:>10} {:>8} {:>12}".format(
                item.get("Item ID"),
                str(item.get("Name"))[:22],
                f"Rs. {item.get('Price', 0):.2f}",
                item.get("Quantity"),
                f"Rs. {sub:.2f}"
            ))
        print("-" * 66)
        print(f"{'Current Total:':>52} Rs. {total:.2f}")
        print("=" * 66)

    def update_order(self):
        if not self.order:
            print("Order is Empty! Nothing to update.")
            return

        try:
            item_id = int(input("Enter the Item ID to update: "))
        except ValueError:
            print("Invalid Item ID! Please enter a number.")
            return

        order_item = next((o for o in self.order if o.get("Item ID") == item_id), None)
        if order_item is None:
            print("Item not found in current order.")
            return

        menu_item = next((m for m in self.menu if m.get("Item ID") == item_id), None)
        if menu_item is None:
            print("Menu item not found. Data mismatch.")
            return

        print("Current quantity:", order_item.get("Quantity"))
        try:
            new_quantity = int(input("Enter the new quantity: "))
        except ValueError:
            print("Invalid quantity! Please enter a number.")
            return

        if new_quantity <= 0:
            print("Quantity must be greater than 0!")
            return

        old_quantity = order_item.get("Quantity", 0)
        quantity_diff = new_quantity - old_quantity

        if quantity_diff > 0:
            if menu_item.get("Stock", 0) < quantity_diff:
                print("Not enough stock available!")
                return
            menu_item["Stock"] -= quantity_diff
        elif quantity_diff < 0:
            menu_item["Stock"] += abs(quantity_diff)

        order_item["Quantity"] = new_quantity
        self.save_menu()
        self.save_orders()
        print("Order updated successfully!")

    def remove_order(self):
        if not self.order:
            print("Order is Empty! Nothing to remove.")
            return

        try:
            item_id = int(input("Enter the Item ID to remove: "))
        except ValueError:
            print("Invalid Item ID! Please enter a number.")
            return

        order_item = next((o for o in self.order if o.get("Item ID") == item_id), None)
        if order_item is None:
            print("Item not found in current order.")
            return

        menu_item = next((m for m in self.menu if m.get("Item ID") == item_id), None)
        if menu_item:
            menu_item["Stock"] += order_item.get("Quantity", 0)

        self.order.remove(order_item)
        self.save_orders()
        self.save_menu()
        print("Item removed from order successfully.")

    def apply_discount(self, grand_total):
        if grand_total >= 5000:
            discount = 0.10
        elif grand_total >= 3000:
            discount = 0.05
        else:
            discount = 0.0

        discounted_total = grand_total * (1 - discount)
        return discounted_total, discount

    def calculate_gst(self, grand_total):
        gst_rate = 0.05
        gst_amount = grand_total * gst_rate
        total_with_gst = grand_total + gst_amount
        return total_with_gst, gst_amount

    def calculate_bill(self):
        if not self.order:
            print("\n======================================")
            print("Order is Empty! Cannot calculate bill.")
            print("======================================")
            return 0

        grand_total = sum(item.get("Price", 0) * item.get("Quantity", 0) for item in self.order)
        discounted_total, discount_rate = self.apply_discount(grand_total)
        total_with_gst, gst_amount = self.calculate_gst(discounted_total)

        print("\n=========================== FINAL BILL ===========================")
        print("{:<8} {:<24} {:>12} {:>8} {:>14}".format("ID", "Name", "Price", "Qty", "Total"))
        print("-" * 68)
        for item in self.order:
            subtotal = item.get("Price", 0) * item.get("Quantity", 0)
            print("{:<8} {:<24} {:>12} {:>8} {:>14}".format(
                item.get("Item ID"),
                str(item.get("Name"))[:22],
                f"Rs. {item.get('Price', 0):.2f}",
                item.get("Quantity"),
                f"Rs. {subtotal:.2f}",
            ))
        print("-" * 68)
        print(f"{'Subtotal:':>52} Rs. {grand_total:>10.2f}")
        if discount_rate > 0:
            print(f"{'Discount (' + str(int(discount_rate * 100)) + '%):':>52} Rs. -{(grand_total - discounted_total):>9.2f}")
            print(f"{'Total after Discount:':>52} Rs. {discounted_total:>10.2f}")
        print(f"{'GST (5%):':>52} Rs. {gst_amount:>10.2f}")
        print("=" * 68)
        print(f"{'Total Payable:':>52} Rs. {total_with_gst:>10.2f}")
        print("==================================================================")

        return total_with_gst

    def choose_order_type(self):
        print("\n==================== ORDER TYPE ====================")
        print("1. Dine-In")
        print("2. Takeaway")
        print("====================================================")

        order_type_choice = input("Enter your choice (1 or 2): ").strip()

        if order_type_choice == "1":
            try:
                table_number = int(input("Table Number (1 to 10): ").strip())
                if table_number < 1 or table_number > 10:
                    print("Invalid table number! Defaulting to Table 1.")
                    return "Dine-In", 1
            except ValueError:
                print("Invalid input! Defaulting to Table 1.")
                return "Dine-In", 1
            return "Dine-In", table_number

        if order_type_choice == "2":
            return "Takeaway", None

        print("Invalid choice! Defaulting to 'Dine-In'.")
        return "Dine-In", 1

    def payment_method(self):
        print("\n==================== PAYMENT METHOD ====================")
        print("1. Cash")
        print("2. Card")
        print("3. Mobile Payment")
        print("========================================================")

        payment_choice = input("Enter your choice (1, 2, or 3): ").strip()

        if payment_choice == "1":
            return "Cash"
        if payment_choice == "2":
            return "Card"
        if payment_choice == "3":
            return "Mobile Payment"

        print("Invalid choice! Defaulting to 'Cash'.")
        return "Cash"

    def checkout(self):
        if not self.order:
            print("Order is Empty! Cannot proceed to checkout.")
            return

        order_type, table_num = self.choose_order_type()
        total_payable = self.calculate_bill()
        
        name = input("\nEnter customer name (leave blank for 'Guest'): ").strip() or "Guest"
        phone = input("Enter customer phone (optional): ").strip()
        payment_type = self.payment_method()

        confirm = input(f"\nProceed to checkout and generate bill for {name}? (y/n): ")
        if confirm.lower() != 'y':
            print("Checkout cancelled.")
            return

        now = datetime.now()
        receipt_number = self.get_next_receipt_number()
        receipt_file = os.path.join("customer_receipts", f"receipt_{receipt_number}.txt")

        lines = []
        lines.append("=" * 60)
        lines.append("{:^60}".format("RESTAURANT RECEIPT"))
        lines.append("=" * 60)
        lines.append(f"Receipt No    : {receipt_number}")
        lines.append(f"Customer      : {name}")
        if phone:
            lines.append(f"Phone         : {phone}")
        lines.append(f"Order Type    : {order_type}" + (f" (Table {table_num})" if table_num else ""))
        lines.append(f"Date & Time   : {now.strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("-" * 60)
        lines.append("{:<6} {:<24} {:>8} {:>18}".format("ID", "Name", "Qty", "Subtotal"))
        lines.append("-" * 60)

        for item in self.order:
            subtotal = item.get("Price", 0) * item.get("Quantity", 0)
            lines.append("{:<6} {:<24} {:>8} {:>18}".format(
                item.get("Item ID"),
                str(item.get("Name", ""))[:22],
                item.get("Quantity"),
                f"Rs. {subtotal:.2f}",
            ))

        lines.append("-" * 60)
        lines.append(f"{'Total Payable:':>38} Rs. {total_payable:.2f}")
        lines.append(f"{'Payment Method:':>38} {payment_type}")
        lines.append("=" * 60)

        bill_text = "\n".join(lines)

        if not os.path.exists("customer_receipts"):
            os.makedirs("customer_receipts")

        with open(receipt_file, "w", encoding="utf-8") as file:
            file.write(bill_text)

        print(f"\n{bill_text}\n")
        print(f"Receipt saved to {receipt_file}")

        self.history.append({
            "Receipt No": receipt_number,
            "Customer Name": name,
            "Phone": phone,
            "Date": now.strftime("%Y-%m-%d"),
            "Time": now.strftime("%H:%M:%S"),
            "Payment Method": payment_type,
            "Order Type": order_type,
            "Table": table_num,
            "Items": [
                {
                    "Item ID": item.get("Item ID"),
                    "Name": item.get("Name"),
                    "Price": item.get("Price"),
                    "Quantity": item.get("Quantity"),
                    "Subtotal": item.get("Price", 0) * item.get("Quantity", 0),
                }
                for item in self.order
            ],
            "Grand Total": total_payable,
        })
        self.save_history()

        self.order.clear()
        self.save_orders()
        self.save_menu()
        print("Thank you for ordering with us!")

    def get_next_receipt_number(self):
        if not os.path.exists("customer_receipts"):
            os.makedirs("customer_receipts")

        receipt_files = [name for name in os.listdir("customer_receipts") if name.startswith("receipt_") and name.endswith(".txt")]
        receipt_numbers = []
        for filename in receipt_files:
            try:
                receipt_numbers.append(int(filename[len("receipt_"): -4]))
            except ValueError:
                continue
        if receipt_numbers:
            return max(receipt_numbers) + 1
        return 1001

    def add_new_item(self):
        print("\n===================== ADD NEW ITEM =====================")
        try:
            item_id = int(input("Enter Item ID: "))
        except ValueError:
            print("Invalid ID! Must be a number.")
            return

        if any(item.get("Item ID") == item_id for item in self.menu):
            print("An item with this ID already exists!")
            return

        name = input("Enter Item Name: ").strip()
        category = input("Enter Category: ").strip()
        try:
            price = float(input("Enter Price: "))
            stock = int(input("Enter Stock Quantity: "))
        except ValueError:
            print("Invalid input for price or stock!")
            return

        new_item = Menu_Item(item_id, name, category, price, stock)
        self.menu.append(new_item.to_dict())
        self.save_menu()
        print(f"Item '{name}' added successfully!")

    def update_item(self):
        print("\n===================== UPDATE ITEM =====================")
        try:
            item_id = int(input("Enter Item ID to update: "))
        except ValueError:
            print("Invalid ID!")
            return

        item = next((i for i in self.menu if i.get("Item ID") == item_id), None)
        if not item:
            print("Item not found!")
            return

        print(f"Updating '{item.get('Name')}' (Press Enter to keep current value)")
        new_name = input(f"New Name [{item.get('Name')}]: ").strip() or item.get('Name')
        new_category = input(f"New Category [{item.get('Category')}]: ").strip() or item.get('Category')
        
        price_input = input(f"New Price [{item.get('Price')}]: ").strip()
        new_price = float(price_input) if price_input else item.get('Price')
        
        stock_input = input(f"New Stock [{item.get('Stock')}]: ").strip()
        new_stock = int(stock_input) if stock_input else item.get('Stock')

        item["Name"] = new_name
        item["Category"] = new_category
        item["Price"] = new_price
        item["Stock"] = new_stock

        self.save_menu()
        print("Item updated successfully!")

    def remove_item(self):
        print("\n===================== REMOVE ITEM =====================")
        try:
            item_id = int(input("Enter Item ID to remove: "))
        except ValueError:
            print("Invalid ID!")
            return

        item = next((i for i in self.menu if i.get("Item ID") == item_id), None)
        if not item:
            print("Item not found!")
            return

        self.menu.remove(item)
        self.save_menu()
        print("Item removed successfully!")

    def view_order_history(self):
        if not self.history:
            print("\nNo order history found.")
            return

        print("\n========================= ORDER HISTORY =========================")
        for record in self.history:
            print(f"Receipt #: {record.get('Receipt No')} | Date: {record.get('Date')} {record.get('Time')} | Customer: {record.get('Customer Name')}")
            print(f"Total: Rs. {record.get('Grand Total', 0):.2f} | Payment: {record.get('Payment Method')}")
            print("-" * 65)

    def view_sales(self):
        if not self.history:
            print("\n==================== SALES REPORT ====================")
            print("No sales data available.")
            print("=======================================================")
            return

        total_sales = sum(order_record.get("Grand Total", 0) for order_record in self.history)
        total_orders = len(self.history)

        print("\n==================== SALES REPORT ====================")
        print(f"Total Orders : {total_orders}")
        print(f"Total Sales  : Rs. {total_sales:.2f}")
        print("=======================================================")

    def admin_login(self):
        admin_username = "admin"
        admin_password = "12345"

        username = input("Enter admin username: ")
        password = input("Enter admin password: ")

        if username == admin_username and password == admin_password:
            print("Admin login successful!")
            return True

        print("Invalid credentials! Access denied.")
        return False

    def admin_menu(self):
        while True:
            print("\n===================== ADMIN MENU ======================")
            print("1. View Menu")
            print("2. Add New Item")
            print("3. Update Item")
            print("4. Remove Item")
            print("5. View Order History")
            print("6. View Sales Report")
            print("0. Exit Admin Menu")
            print("=========================================================")

            try:
                choice = int(input("Enter option number: "))
            except ValueError:
                print("Invalid Choice! Please enter a number.")
                continue

            if choice == 1:
                self.view_menu()
            elif choice == 2:
                self.add_new_item()
            elif choice == 3:
                self.update_item()
            elif choice == 4:
                self.remove_item()
            elif choice == 5:
                self.view_order_history()
            elif choice == 6:
                self.view_sales()
            elif choice == 0:
                print("Exiting Admin Menu...")
                return
            else:
                print("Invalid choice! Please try again.")

    def customer_menu(self):
        while True:
            print("\n=============== CUSTOMER MENU ===============")
            print("1. View Menu")
            print("2. Search Food Item")
            print("3. Place Order")
            print("4. View Current Order")
            print("5. Update Order")
            print("6. Remove Item from Order")
            print("7. Calculate Bill")
            print("8. Checkout")
            print("0. Back to Main Menu")
            print("=============================================")

            try:
                choice = int(input("Enter option number: "))
            except ValueError:
                print("Invalid Choice! Please enter a number.")
                continue

            if choice == 1:
                self.view_menu()
            elif choice == 2:
                self.search_food()
            elif choice == 3:
                self.place_order()
            elif choice == 4:
                self.view_current_order()
            elif choice == 5:
                self.update_order()
            elif choice == 6:
                self.remove_order()
            elif choice == 7:
                self.calculate_bill()
            elif choice == 8:
                self.checkout()
            elif choice == 0:
                return
            else:
                print("Invalid choice! Please try again.")

    def exit_system(self):
        print("\nThank you for ordering with us!")
        print("Good Bye! Have a nice day!")
        print("Exiting the Restaurant Order System...")
        sys.exit()


def main_menu():
    restaurant_manager = Restaurant_Manager(menu=[], order=[], history=[], users=[], discounts=[], sales=[])
    restaurant_manager.load_menu()
    restaurant_manager.load_orders()
    restaurant_manager.load_history()
    restaurant_manager.load_users()

    while True:
        print("\n=============== Welcome to the Restaurant Order System ===============")
        print("1. Order as Customer")
        print("2. Login as Admin")
        print("0. Exit")
        print("======================================================================")

        choice = input("Enter your choice (1, 2, or 0): ").strip()

        if choice == "1":
            restaurant_manager.customer_menu()
        elif choice == "2":
            if restaurant_manager.admin_login():
                restaurant_manager.admin_menu()
        elif choice == "0":
            restaurant_manager.exit_system()
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main_menu()