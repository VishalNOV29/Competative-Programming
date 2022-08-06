from typing import NamedTuple


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Simple :",self.name)
        name=self.name
        print("Advance :",name)
obj1=Student("Vishal kumar singh",22)
obj1.display()