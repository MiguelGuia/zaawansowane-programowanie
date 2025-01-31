'''1. Stworzyć strukturę plików i katalogów, jak powyżej. Następni
a. w module Product i Order zaimportować moduł util
b. w module main zaimportować jedynie moduł Product'''



from magazine.Product import Product  

if __name__ == "__main__":
   
    product1 = Product("Laptop", 1200.50)
    product2 = Product("Smartphone", 800.75)

    print(product1)
    print(product2)