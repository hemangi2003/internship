"""
Exercise: E001-V3 :

Create one class named “location” with members “name”, “code”.
Create one class named “movement” with members “from_location”, “to_location”, “product”, “quantity”.
Create one static method named “movements_by_product” inside the “movement” class with one argument named “product”.
This method will return all “movement” objects which belong to the passed “product” as an argument.
Add new members inside the product “stock_at_locations”. This new member is a type of Dictionary and,
it contains “location” as key and actual stock of that product on that location as value.
Create 4 different location objects.
Create 5 different product objects.
Move those 5 products from one location to another location using movement.
Manage exceptions if product stock goes in -ve.
Display movements of each product using the “movement_by_product” method.
Display product details with its stock at various locations using “stock_at_locations”.
Display product list by location ( group by location).
"""


class Location:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __str__(self):
        return f"name: {self.name}\n code: {self.code}"


# Add new members inside the product “stock_at_locations”. This new member is a type of Dictionary and,
# it contains “location” as key and actual stock of that product on that location as value.
class Product:
    def __init__(self, code, name, category, price):
        self.code = code
        self.name = name
        self.category = category
        self.price = price
        self.stock_at_locations = {}

    def __str__(self):
        return f"category:{self.category}\nCode:{self.code}\nName:{self.price}"

    @staticmethod
    def product_stock_details():
        for h in P:
            print("Product Code:", h.code)
            print("Product Name:", h.name)
            print("Product Category:", h.category)
            print("Product Price:", h.price)
            print("Product Stock at locations:", h.stock_at_locations)
            print("\n")

    @staticmethod
    def product_list(location_name):
        print(f"Location: {location_name}")
        for product_d in P:
            if location_name in product_d.stock_at_locations :
                print(product_d.name, ":-", product_d.stock_at_locations[location_name])
                # print(product_d.stock_at_locations[location_name].quantity)
        print()


class Movement:
    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity
        self.movements = []

    # Create one static method named “movements_by_product” inside the “movement” class with one argument
    # named“product”. This method will return all “movement” objects which belong to the passed “product” as an argument.
    def movements_by_product(product_name):
        for x in range(len(Movements)):
            if Movements[x].product.name == product_name:
                print("From ", Movements[x].from_location.name, "to ", Movements[x].to_location.name, "Product:-",
                      Movements[x].product.name, ",", "quantity of product:", Movements[x].quantity)

                if P[i].stock_at_locations == {}:
                    for y in range(len(location_list)):
                        if location_list[y].name == Movements[x].to_location.name:
                            P[i].stock_at_locations[location_list[y].name] = Movements[x].quantity
                        # else:
                        #     P[i].stock_at_locations[location_list[y].name] = 0
                elif P[i].stock_at_locations != {} and len(P[i].stock_at_locations) == len(location_list):
                    for y in range(len(location_list)):
                        if location_list[y].name == Movements[x].to_location:
                            P[i].stock_at_locations[location_list[y].name] += Movements[x].quantity
                # else:
                #     if P[i].stock_at_locations[Movements[x].from_location.name] >= Movements[x].quantity:
                #         P[i].stock_at_locations[Movements[x].from_location.name] -= Movements[x].quantity
                #         # decreasing the in product quantity at particular location
                #         P[i].stock_at_locations[Movements[x].to_location.name] += Movements[x].quantity
                #     # increasing in product quantity at particular location
                #     else:
                #         print(P[i].name, "product Stock is less")


# Create 4 different location objects.

Location1 = Location("Rajkot", "l1")
Location2 = Location("Ahmedabad", "l2")
Location3 = Location("Bhuj", "l3")
Location4 = Location("Gandhinagar", "l4")

location_list = [Location1, Location2, Location3, Location4]

# Create 5 different product objects.
# P1 = Product("p001", "Honda", "vehicle", 100000,
#              {Location1.name: 50, Location2.name: 30, Location3.name: 0, Location4.name: 0})
# P2 = Product("p002", "Kia", "car", 200000,
#              {Location1.name: 0, Location2.name: 30, Location3.name: 20, Location4.name: 0})
# P3 = Product("p003", "Mountain", "cycle", 30000,
#              {Location1.name: 0, Location2.name: 0, Location3.name: 40, Location4.name: 0})
# P4 = Product("p004", "KTM", "bike", 40000,
#              {Location1.name: 0, Location2.name: 0, Location3.name: 0, Location4.name: 10})
# P5 = Product("p005", "TATA", "vehicle", 50000,
#              {Location1.name: 15, Location2.name: 0, Location3.name: 0, Location4.name: 0})

P1 = Product("p001", "Honda", "vehicle", 100000)
P2 = Product("p002", "Kia", "car", 200000)
P3 = Product("p003", "Mountain", "cycle", 30000)
P4 = Product("p004", "KTM", "bike", 40000)
P5 = Product("p005", "TATA", "vehicle", 50000)

P = [P1, P2, P3, P4, P5]

Movement1 = Movement(Location1, Location2, P1, 4)
Movement2 = Movement(Location3, Location4, P2, 3)
Movement3 = Movement(Location2, Location3, P3, 2)
Movement4 = Movement(Location4, Location1, P4, 5)
Movement5 = Movement(Location3, Location2, P5, 1)
Movement6 = Movement(Location1, Location3, P1, 10)
Movement7 = Movement(Location4, Location3, P2, 5)

Movements = [Movement1, Movement2, Movement3, Movement4, Movement5, Movement6]

# Display product details with its stock at various locations using “stock_at_locations”.
Product.product_stock_details()

# Display movements of each product using the “movement_by_product” method.
for i in range(len(P)):
    print(P[i].code, P[i].name)
    Movement.movements_by_product(P[i].name)
    print("\n")

# Display product list by location ( group by location).
for location in location_list:
    Product.product_list(location.name)

print("product details with stock at locations using “stock_at_locations” after movement.")

Product.product_stock_details()
