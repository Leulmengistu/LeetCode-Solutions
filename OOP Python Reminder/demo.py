from abc import ABC, abstractmethod

class Computer(ABC):


    '''
    Abstract methods: are methods that only have declaration but not definition.
    meaning a function is said to be declared in python when it is given a name and the body is pass.

    Abstract Class: is a class that only has Abstract methods

    To make a class abstract it needs to import the ABC module and abstractmethod module.
    ABC - stands for Abstract Base Class 
    For abstract methods we use a decorator @abstractmethod

    Python does not support abstract class and method like other languages

    Abstract classes can't have instances

    The difference between an Interface and an Abstract class is they are both Abstract classes but the only differnce
    is that for interface all the abstract methods should be empty while for abstract classes the abstract methods
    may not be empty 
    '''
    @abstractmethod
    def process(self):
        print("running")


class Laptop(Computer):

    def process(self):
        print("it is running")

class Whiteboard(Computer):
    def write(self):
        print("its writting")
    def process(self):
        return super().process()

class Programmer:

    def work(self,com):
        print("solving problems")
        com.process()


com1 = Laptop()

com2 = Whiteboard()

prog1 = Programmer()

prog1.work(com2)
prog1.work(com1)