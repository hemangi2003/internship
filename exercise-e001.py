# Create one class named "category" with members "name", "code", "no_of_products"
class category:
    def __init__(self,name,code):
        self.name = name
        self.code = code
        self.no_of_product = 0

    def __str__(self):
        return f"Category: {self.name}\nCode: {self.code}\nNumber of Products: {self.no_of_product}"
# Create one class named "product" with members "name", "code", "category", "Price"
class product:
    def __init__(self,name,code,category,price):
        self.name=name
        self.code=code
        self.category=category
        self.price=price
    def __str__(self):
        return f"Name: {self.name}\nCode: {self.code}\nCategory: {self.category.name}\nPrice: {self.price:}"
# Create three objects of a category.
category1 = category("electronics", "CAT001")
category2 = category("clothing", "CAT002")
category3 = category("home Decor", "CAT003")

# Create 10 different products

products = [ product("lenovo","e001",category1,41000),
product("hp","e002",category1,30000),
product("hp","e003",category1,20000),
product("fen","e004",category1,5000),
product("top","e005",category2,2000),
product("dress","e006",category2,1500),
product("jeans","e007",category2,800),
product("saree","e008",category2,7000),
product("photo frame","e009",category3,600),
product("clock","e010",category3,1000)]


# Update the no_of_products for each category
for product in products:
    product.category.no_of_product += 1

# Print category info with its no_of_products
print(category1,"\n")
print(category2,"\n")
print(category3,"\n")

# Sort and Print products based on price ( Price High to Low and Low to High) with all details.

# Sort and print products based on price (high to low)
print("Products Sorted by Price (High to Low):")
products_high_to_low = sorted(products, key=lambda x: x.price, reverse=True)
for product in products_high_to_low:
    print(product)
    print("\n")

# Sort and print products based on price (low to high)
print("Products Sorted by Price (Low to High):")
products_low_to_high = sorted(products, key=lambda x: x.price, reverse=False)
for product in products_low_to_high:
    print(product)
    print("\n")

print("Enter Search Code: ")
s_code = input()
search_code = s_code
for product in products:
    if product.code == search_code:
        print(f"\nProduct found by code {search_code}: {product}")
        break
else:
    print(f"\nProduct with code {search_code} not found.")