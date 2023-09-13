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

        # Update the no_of_products for each category
        category.no_of_product += 1

    def __str__(self):
        return f"Name: {self.name}\nCode: {self.code}\nCategory: {self.category.name}\nPrice: {self.price:}"
    def HightoLowPrice():
        n = len(products)
        for i in range(n):
            for j in range(0, n - i - 1):
                if products[j].price < products[j + 1].price:
                    products[j], products[j + 1] = products[j + 1], products[j]
        print(f"Products Sorted by Price (High to Low):")
        for product in products:
            print("\n", product)

    def LowtoHighPrice():
        n = len(products)
        for i in range(n):
            for j in range(0, n - i - 1):
                if products[j].price > products[j + 1].price:
                    products[j], products[j + 1] = products[j + 1], products[j]
        print(f"Products Sorted by Price (Low to high):")
        for product in products:
            print("\n", product)

    def SearchCode(scode):
        for product in products:
            if product.code == scode:
                print(f"\nProduct found by code {scode}:\n{product}")
                break
        else:
            print(f"\nProduct with code {scode} not found.")


# Create three objects of a category.
category1 = category("electronics", "C001")
category2 = category("clothing", "C002")
category3 = category("home Decor", "C003")

# Create 10 different products
products = [ product("lenovo","e001",category1,41000),
product("hp","e002",category1,30000),
product("hp","e003",category1,20000),
product("fen","e004",category1,5000),
product("top","e005",category2,2000),
product("dress","e006",category2,1500),
product("jeans","e007",category3,800),
product("saree","e008",category3,7000),
product("photo frame","e009",category3,600),
product("clock","e010",category3,1000)]

# Print category info with its no_of_products
print(category1,"\n")
print(category2,"\n")
print(category3,"\n")

# Sort and Print products based on price ( Price High to Low and Low to High) with all details.

# Sort and print products based on price (high to low)
product.HightoLowPrice()

# Sort and print products based on price (low to high)
product.LowtoHighPrice()

#Search product using its code
product.SearchCode("e009")
