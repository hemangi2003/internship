"""
Create a new class named "Customer" with below members. "name","email","phone","street","city","state","country","company","type".
"type" must be from "company,contact,billing,shipping".
"Company" must be a Customer object which is the parent object.
Apply Multiple possible validation for phone number and email
Does not allowed number in name,city,state and country

Create a new class named "Order" with members "number","date", "company", "billing", "shipping", "total_amount","order_lines".
"company", "billing", "shipping" are objects of Customer.
"date" must be today or the future. Does not allow past date.
"total_amount" auto calculated based on different products inside order.
"order_lines" is list of objects of "OrderLine"

create a new class named "OrderLine" with members "order", "product", "quantity", "price", "subtotal".
"order" is the object of Order.
"subtotal" is auto calculated based on quantity and price.

Display Order and Customer Information Sort orders based on "date".
User can filter the current month orders Search Orders from its number.
List/Display all orders of a specific product.
"""
import re
from datetime import datetime
from datetime import date


class Customer:
    def __init__(self, name, email, phone, street, city, state, country, company, type):
        self.name = self.validate_name(name)
        self.email = self.validate_email(email)
        self.phone = self.validate_phone(phone)
        self.street = street
        self.city = self.validate_name(city)
        self.state = self.validate_name(state)
        self.country = self.validate_name(country)
        self.company = company
        self.type = self.validate_type(type)

    def validate_name(self, name):
        if any(char.isdigit() for char in name):
            print("not valid name.")
        return name

    def validate_email(self, email):
        regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if not re.match(regex, email):
            print("not valid email address.")
        return email

    def validate_phone(self, phone):
        regex = r'(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}'
        if not re.match(regex, phone):
            print("not valid phone number.")
        return phone

    def validate_type(self, type):
        if type not in ['company', 'contact', 'billing', 'shipping']:
            print("type is not match")
        return type

    @staticmethod
    def Customer_info():
        for a in C:
            print("Customer Name:-", a.name)
            print("Customer email:-", a.email)
            print("Customer Phone:-", a.phone)
            print("Customer street:-", a.street)
            print("Customer City:-", a.city)
            print("Customer State:-", a.state)
            print("Customer Country:-", a.country)
            print("Customer Type:-", a.type)
            print('\n')


class Order:
    def __init__(self, number, date1, company, billing, shipping):
        self.number = number
        self.date = self.validate_date(self, date1)
        self.company = company
        self.billing = billing
        self.shipping = shipping
        self.total_amount = 0
        self.order_lines = []

    @staticmethod
    def validate_date(self, date1):
        date_object = datetime.strptime(date1, '%d-%m-%Y').date()
        today = date.today()
        if date_object < today:
            print("Does not allow past date")
        return date1

    def add_orderline(self, order_line):
        self.order_lines.append(order_line)
        self.total_amount += order_line.subtotal

    # display orderlines info
    def display_order_lines(self):
        print(f"Order Number: {self.number}")
        print(f"Order Company: {self.company} \nBilling Company: {self.billing} \nShipping Company: {self.shipping}")
        print("Order Lines:")
        for line in range(len(self.order_lines)):
            print(
                f" {line + 1}. Product: {self.order_lines[line].product}, Quantity: {self.order_lines[line].quantity}, Price: {self.order_lines[line].price}, Subtotal: {self.order_lines[line].subtotal}")

    # Sort orders based on "date"
    @staticmethod
    def sort_orders():
        n = len(order_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                if datetime.strptime(order_list[j].date, '%d-%m-%Y').date() > datetime.strptime(order_list[j + 1].date,
                                                                                                '%d-%m-%Y').date():
                    order_list[j], order_list[j + 1] = order_list[j + 1], order_list[j]
        print(f"Order Sorted by Date")
        print('--------------------------------')
        for orders in order_list:
            print("Order Date:", orders.date)
            print(
                f"Order No: {orders.number}, Order Company: {orders.company} \n")

    @staticmethod
    def Sort_order_Current_Month():
        print(f"Order Sorted by Month")
        print('--------------------------------')
        for i in order_list:
            if datetime.strptime(i.date, '%d-%m-%Y').month == datetime.now().month:
                print("Order Date:", i.date)
                print(
                    f"Order No: {i.number}, Order Company: {i.company} \n")

    @staticmethod
    def search_order():
        search_order = input("Enter Search Orders number(write like o1): ")
        for o in order_list:
            if o.number.lower() == search_order.lower():
                o.display_order_lines()
                print(f"Total Amount: {o.total_amount}")

    @staticmethod
    def search_product():
        search_product = input("Enter Search Product Name: ")
        print(f"Order Details: \n")
        for o in ol:
            if o.product.lower() == search_product.lower():
                print(
                    f"Company Name: {o.order.company}\nBilling Company Name: {o.order.billing} \nShipping Company Name: {o.order.shipping}")
                print(f"Quantity: {o.quantity}, Price: {o.price}, Subtotal: {o.subtotal} \n")


class OrderLine:
    def __init__(self, Order, product, quantity, price):
        self.order = Order
        self.product = product
        self.quantity = quantity
        self.price = price
        self.subtotal = self.calculate_subtotal(quantity, price)
        # "subtotal" is auto  calculated based on quantity and price

    # calculate a subtotal
    @staticmethod
    def calculate_subtotal(quantity, price):
        calculate_subtotal = quantity * price
        return calculate_subtotal


# Customers objects
Customer1 = Customer("CustomerR", "company@example.com", "+123456789", "Company St", "Rajkot", "Gujarat", "India", None,
                     type="company")
Customer2 = Customer("CustomerA", "billing@example.com", "+987654321", "Billing St", "Ahmedabad", "Gujarat", "India",
                     Customer1, type="billing")
Customer3 = Customer("CustomerG", "shipping@example.com", "+111222333", "Shipping St", "Gandhinagar", "Gujarat",
                     "India", Customer1, type="shipping")
Customer4 = Customer("CustomerB", "companyb@example.com", "+124038401", "CompanyB St", "Bangalore", "Karnataka",
                     "India", None, type="company")
Customer5 = Customer("CustomerP", "billingp@example.com", "+937654321", "BillingP St", "Pune", "Maharashtra", "India",
                     Customer4, type="billing")
Customer6 = Customer("CustomerH", "shippingh@example.com", "+113222333", "ShippingH St", "Hyderabad", "Telangana",
                     "India", Customer4, type="shipping")

C = [Customer1, Customer2, Customer3, Customer4, Customer5, Customer6]

# "order" is the object of Order.
order1 = Order("o1", "11-02-2024", "CustomerR", "CustomerA", "CustomerG")
order2 = Order("o2", "30-01-2024", "CustomerB", "CustomerP", "CustomerH")
order3 = Order("o3", "12-03-2024", "CustomerR", "CustomerR", "CustomerR")

order_list = [order1, order2, order3]

# orderline objects
order_line1 = OrderLine(order1, "Honda", 2, 150000)
order_line2 = OrderLine(order2, "Kia", 1, 200000)
order_line3 = OrderLine(order1, "Mountain", 3, 22000)
order_line4 = OrderLine(order2, "Honda", 4, 300000)

ol = [order_line1, order_line2, order_line3, order_line4]

# add the orderline in to the order_lines
for i in order_list:
    for j in ol:
        if i.company == j.order.company:
            i.add_orderline(j)

# print("Customer Information: \n")
# Customer.Customer_info()
print('--------------------------------')
print("order_lines is list of objects of OrderLine")
print('--------------------------------')
# display the order and orderlines
for k in order_list:
    k.display_order_lines()
    print('-----------')
    print(f"Total Amount: {k.total_amount}")
    print('----------- \n')

print('--------------------------------')
Order.sort_orders()
print('--------------------------------')
# filter the current month orders
Order.Sort_order_Current_Month()
print('--------------------------------')
# Search Orders from its number.
Order.search_order()
print('--------------------------------')
# List/Display all orders of a specific product.
Order.search_product()
