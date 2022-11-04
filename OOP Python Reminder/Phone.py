import csv
from Item import Item
class Phone(Item):

   
    def __init__(self,name:str="",price:float=0.0,quantity:int=0,broken_phone:int=0):

        super().__init__(name,price,quantity)
        # Run validation on recived arguments
        assert broken_phone >=0 , f"Broken Phone numbers {broken_phone} is not greater than or equal to zero. Broken phone numbers must be non negative"
        # Assign value to self object
        
        self.broken_phone = broken_phone
       