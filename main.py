# Kreiranje main.py datoteke
from product import Product
from product_manager import ProductManager

if __name__ == "__main__":
    manager = ProductManager()
    product1 = Product("Laptop", 1000, 5)
    product2 = Product("Telefon", 500, 10)
    product3 = Product("Slusalice", 100, 15)

    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)

    manager.display_products()
    print("Total Inventory Value:", manager.total_inventory_value())
