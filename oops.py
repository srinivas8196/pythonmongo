class person:
    age = 35
    name = "Srinivas"
    phone = "123456789"

class shop:
    pname= ""
    price= ""
    category = ""

    def __init__(self,pname,price,category):
        self.pname = pname
        self.price = price
        self.category = category


def hobby():
    print("I like to watch movies")

classobj = shop("iphone11","120000","mobiles")
print("product name:"+classobj.pname)
print("product price: "+classobj.price)
print("product category:"+classobj.category)

hobby()