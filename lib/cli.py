# lib/cli.py
from lib.helpers import (
    add_customer, view_customers, delete_customer,
    add_supplier, view_suppliers, delete_supplier,
    add_part, view_parts, delete_part,
    add_order, view_orders
)

def main_menu():
    print("\n=== EV Spare Parts Inventory & Order Management ===")
    print("1. Manage Customers")
    print("2. Manage Suppliers")
    print("3. Manage Parts")
    print("4. Manage Orders")
    print("0. Exit")

def customer_menu():
    print("\n--- Customers ---")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Delete Customer")
    print("0. Back to Main Menu")

def supplier_menu():
    print("\n--- Suppliers ---")
    print("1. Add Supplier")
    print("2. View Suppliers")
    print("3. Delete Supplier")
    print("0. Back to Main Menu")

def part_menu():
    print("\n--- Parts ---")
    print("1. Add Part")
    print("2. View Parts")
    print("3. Delete Part")
    print("0. Back to Main Menu")

def order_menu():
    print("\n--- Orders ---")
    print("1. Add Order")
    print("2. View Orders")
    print("0. Back to Main Menu")


def main():
    while True:
        main_menu()
        choice = input("> ")

        if choice == "0":
            print("Exiting program. Goodbye!")
            break
        elif choice == "1":
            while True:
                customer_menu()
                c_choice = input("> ")
                if c_choice == "0":
                    break
                elif c_choice == "1":
                    name = input("Customer Name: ")
                    phone = input("Phone (optional): ")
                    email = input("Email (optional): ")
                    add_customer(name, phone, email)
                elif c_choice == "2":
                    view_customers()
                elif c_choice == "3":
                    cid = int(input("Customer ID to delete: "))
                    delete_customer(cid)
                else:
                    print("Invalid option.")
        elif choice == "2":
            while True:
                supplier_menu()
                s_choice = input("> ")
                if s_choice == "0":
                    break
                elif s_choice == "1":
                    name = input("Supplier Name: ")
                    contact = input("Contact (optional): ")
                    address = input("Address (optional): ")
                    add_supplier(name, contact, address)
                elif s_choice == "2":
                    view_suppliers()
                elif s_choice == "3":
                    sid = int(input("Supplier ID to delete: "))
                    delete_supplier(sid)
                else:
                    print("Invalid option.")
        elif choice == "3":
            while True:
                part_menu()
                p_choice = input("> ")
                if p_choice == "0":
                    break
                elif p_choice == "1":
                    name = input("Part Name: ")
                    category = input("Category: ")
                    price = float(input("Price: "))
                    supplier_id = int(input("Supplier ID: "))
                    stock_quantity = int(input("Stock Quantity (default 0): ") or 0)
                    min_stock = int(input("Min Stock (default 5): ") or 5)
                    add_part(name, category, price, supplier_id, stock_quantity, min_stock)
                elif p_choice == "2":
                    view_parts()
                elif p_choice == "3":
                    pid = int(input("Part ID to delete: "))
                    delete_part(pid)
                else:
                    print("Invalid option.")
        elif choice == "4":
            while True:
                order_menu()
                o_choice = input("> ")
                if o_choice == "0":
                    break
                elif o_choice == "1":
                    customer_id = int(input("Customer ID: "))
                    part_id = int(input("Part ID: "))
                    quantity = int(input("Quantity: "))
                    add_order(customer_id, part_id, quantity)
                elif o_choice == "2":
                    view_orders()
                else:
                    print("Invalid option.")
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
