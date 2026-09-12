products = {101: {"name": "Laptop","category":"Electronics","price": 55000, "stock": 10 },102: {"name": "Mobile","category":"Electronics","price": 19000, "stock": 20 }}

def Add_product():
    product_id=int(input("Enter Id: "))

    if product_id in products:
        print("product id Exists")
        return

   
    product_name=input("Enter Pdname: ")
    product_category=input("Enter pdcategory: ")
    product_Price=eval(input("Enter pdprice: "))
    product_stock=int(input("Enter Stock: "))

    products[product_id]={
    "name": product_name,
    "category": product_category,
    "price": product_Price,
    "stock": product_stock
    }
    print("Product Added Sucessfully")


# 2.update_stock
def update_stock():

    pid=int(input("Enter id: "))

    if pid  in products:
      n_stock=int(input("Enter new stock: "))
      products[pid]["stock"]= products[pid]["stock"]+n_stock
      print("Stock updated")
    else:
       print("not done")

# print(update_stock())
# print(products) 

# 3.update_productprice
def update_price():
    id=eval(input("Enter id: ")) 

    if id in products:
        chnage_pdprice=int(input("Enter updated productprice: "))
        products[id]["price"]=chnage_pdprice
        print("update successfully")
    else:
        print("product not found")

# print(update_price())
# print(products)

# 4.Search product.
def search_product():
    ids = int(input("Enter id: "))

    if ids in products:
        print("Product found")
        print("Product ID :", ids)
        print("Product Name :", products[ids]["name"])
        print("Category :", products[ids]["category"])
        print("Price :", products[ids]["price"])
        print("Stock :", products[ids]["stock"])

    else:
        print("Product not found") 

# print(search_product())

# 5.Display All products
def display():
    print('-'*105)
    print(f"|{'Pid':>20}|{'Product Name':>20}|{'category':>20}|{'price':>20}|{'stock':>20}")
    print('-'*105)
    for pid,pdata in products.items():
        print(f"|{pid:>20}|{pdata["name"]:>20}|{pdata['category']:>20}|{pdata['price']:>20}|{pdata['stock']:>20}")
# print(display())

# 6.menu:
def menu():
    while True:
        print('''
================ PRODUCT MANAGEMENT SYSTEM ======================
        1.Add Product
        2.Update Stock
        3.Update Product_price
        4.Search Product
        5.Display All_products
        6.Exist
===================================================================
''')  
        choice=int(input("Enter Choice: "))
        if choice==1:
            Add_product()
        elif choice==2:
            update_stock()
        elif choice==3:
            update_price()
        elif choice==4:
            search_product()
        elif choice==5:
            display()
        elif choice==6:
            print("Thank You")
            break
        else:
            print("Invalid Choice")


print(menu())