# Exercise: E001-V2
#
# •	Add new data members “parent”, “display_name”, and “products” (list of Product objects) inside the Category class.
# •	Add a new member function to generate “display_name”.
# •	“display_name” has the text value as below.
#            1.	Vehicle Category without parent then “Vehicle”
#            2.	Car Category with “Vehicle” as a parent then “Vehicle > Car”
#            3.	Petrol Category with “Car” as a parent then “Vehicle > Car > Petrol”
# •	Create 5 Category objects with parent and child relation.
# •	Create 3 Product objects in each Category.
# •	Display the Category with its Code, Display Name, and all Product details inside that Category.
# •	Display Product list by Category (group by Category, order by Category name).

class Product:
    def __init__(self, code, name, category, price):
        self.code = code
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f"category:{self.category}\nCode:{self.code}\nName:{self.price}"


class Category:
    def __init__(self, name, code, parent=None):
        self.name = name
        self.code = code
        self.parent = parent
        self.display_name = self.generate_display_name()
        self.products = []

    def __str__(self):
        return f"Category:{self.name}\nCode:{self.code}\nDisplay Name:{self.display_name}\n\nProducts:\n{self.products}"

    def generate_display_name(self):
        if self.parent is not None:
            return f"{self.parent.generate_display_name()}>{self.name}"
        else:
            return f"{self.name}"

    @staticmethod
    def display():
        for category in [vehicle, car, petrol, cycle, bike]:
            print(f"Category Code: {category.code}")
            print(f"Category Display Name: {category.display_name}")
            for product in category.products:
                print(f"Product Name: {product.name}")
                print(f"Product Code: {product.code}")
                print(f"Product Price: {product.price}")
                print(" ")

    @staticmethod
    def product_list():
        for i in categories:
            print(f"Products in {i.name}:")
            for product_d in i.products:
                print(f" {product_d.name}")
            print()

# Create 5 Category objects with parent and child relation
vehicle = Category("vehicle", "v1")
car = Category("car", "c1", vehicle)
petrol = Category("petrol", "p1", car)
cycle = Category("cycle", "hero", petrol)
bike = Category("bike", "bike", cycle)
# Create 3 Product objects in each Category.
products = [Product("p001", "p1", vehicle, 1000),
            Product("p002", "p2", car, 2000),
            Product("p003", "p3", cycle, 3000),
            Product("p004", "p4", bike, 4000),
            Product("p005", "p5", vehicle, 5000),
            Product("p006", "p6", petrol, 6000),
            Product("p007", "p7", bike, 7000),
            Product("p008", "p8", cycle, 8000),
            Product("p009", "p9", car, 9000),
            Product("p010", "p10", petrol, 10000),
            Product("p011", "p11", vehicle, 11000),
            Product("p012", "p12", bike, 12000),
            Product("p013", "p13", car, 13000),
            Product("p014", "p14", cycle, 14000),
            Product("p015", "p15", petrol, 15000)]

categories = [vehicle, car, petrol, cycle, bike]

for p in products:
    p.category.products.append(p)

# Display the Category with its Code, Display Name, and all Product details inside that Category.

Category.display()

# Display product list by category (group by category, order by category name)
Category.product_list()
