# lib/helpers.py
from lib.models import Customer, Supplier, Part, Order
from setup_db import session

# CUSTOMER CRUD

def add_customer(name, phone=None, email=None):
    customer = Customer(name=name, phone=phone, email=email)
    session.add(customer)
    session.commit()
    print(f"Customer '{name}' added successfully!")

def view_customers():
    customers = session.query(Customer).all()
    for c in customers:
        print(c)

def delete_customer(customer_id):
    customer = session.query(Customer).get(customer_id)
    if customer:
        session.delete(customer)
        session.commit()
        print(f"Customer ID {customer_id} deleted successfully!")
    else:
        print("Customer not found.")


#  SUPPLIER CRUD

def add_supplier(name, contact=None, address=None):
    supplier = Supplier(name=name, contact=contact, address=address)
    session.add(supplier)
    session.commit()
    print(f"Supplier '{name}' added successfully!")

def view_suppliers():
    suppliers = session.query(Supplier).all()
    for s in suppliers:
        print(s)

def delete_supplier(supplier_id):
    supplier = session.query(Supplier).get(supplier_id)
    if supplier:
        session.delete(supplier)
        session.commit()
        print(f"Supplier ID {supplier_id} deleted successfully!")
    else:
        print("Supplier not found.")


# PART CRUD

def add_part(name, category, price, supplier_id, stock_quantity=0, min_stock=5):
    part = Part(
        name=name, category=category, price=price,
        supplier_id=supplier_id, stock_quantity=stock_quantity,
        min_stock=min_stock
    )
    session.add(part)
    session.commit()
    print(f"Part '{name}' added successfully!")

def view_parts():
    parts = session.query(Part).all()
    for p in parts:
        print(p)

def delete_part(part_id):
    part = session.query(Part).get(part_id)
    if part:
        session.delete(part)
        session.commit()
        print(f"Part ID {part_id} deleted successfully!")
    else:
        print("Part not found.")


#  ORDER CRUD

def add_order(customer_id, part_id, quantity):
    order = Order(customer_id=customer_id, part_id=part_id, quantity=quantity)
    # calculate total price
    part = session.query(Part).get(part_id)
    if part:
        order.total_price = part.price * quantity
        # decrease stock quantity
        if part.stock_quantity >= quantity:
            part.stock_quantity -= quantity
        else:
            print("Warning: Not enough stock!")
            return
        session.add(order)
        session.commit()
        print(f"Order for Customer ID {customer_id} added successfully!")
    else:
        print("Part not found.")

def view_orders():
    orders = session.query(Order).all()
    for o in orders:
        print(o)
