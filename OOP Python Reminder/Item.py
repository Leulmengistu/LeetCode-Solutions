import csv
class Item:

    pay_rate = 0.8 # is a class attribute
# In OOP python we have two types of attributes the instance attributes and class attributes

    all = []
    def __init__(self,name:str="",price:float=0.0,quantity:int=0):

        # Run validation on recived arguments
        assert price >=0 , f"Price {price} is not greater than or equal to zero. Price must be non negative"
        assert quantity >=0, f"Quantity {quantity} is not greater than or equal to zero. Quantity must be non negative"

        # Assign value to self object
        self.__name = name
        self.__price=price
        self.__quantity=quantity
        # print("Superclass constructor")
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__name} , {self.__price}, {self.__quantity})"

    def calculate_total_price(self):
        return self.__price*self.__quantity

    @classmethod
    def instantiate_from_csv(cls):

        with open("items.csv","r") as f:

            reader = csv.DictReader(f)
            items = list(reader)
    

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):

        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

    def apply_discount(self):
        self.price =  self.__price * self.pay_rate
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def setname(self,name):
        self.__name = name

    @property
    def getprice(self):
        return self.__price

    @getprice.setter
    def setprice(self,price):
        if price < 0:
            raise Exception("Price cannot be less than zero")
        else:
            self.__price = price
    
    def getname(self):
        return self.__name

    @property
    def getquantity(self):
        return self.__quantity
    

    @getquantity.setter
    def setquantity(self,quantity):
        if quantity < 0:
            raise Exception ("Quantity cannot be less than zero")
        else:
            self.__quantity = quantity
        
'''
Encapsulation: is to cover or protect the attributes from being directly manipulated by using a setter and getter methods.
Abstraction: is hiding the unneccessary informations
inheritance : is a mechanism that lets us reuse code across our classes.
polymorphism: is a class can implement an inherited method in its own way
'''





# item1 = Item("Phone",100,3)
# item2 = Item("laptop",1000,3)
# item3 = Item("Cable",10,5)
# item4 = Item("Mouse",50,5)
# item6 = Item("Keyboard",75,5)


# print(Item.pay_rate) # class attributes can be accessed without an instance  with just the class

# print(Item.__dict__) # Prints all the attributes that belong to the class

# print(item1.__dict__) # prints all the attributes that belong to the instance


