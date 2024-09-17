# Here is another example of class and object
class Animal():
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
    def Era(self):
        return f"Name of the animal is {self.name} and age of the animal is {self.age},colour {self.color}"
    def Owner(self):
        return f" Happy with my pet"
A=Animal("shiru",2.3,"black")
B=Animal("YUYU",3,"white")
print(A.Era())
print(A.Owner())
print(B.Era())
print(B.Owner())
