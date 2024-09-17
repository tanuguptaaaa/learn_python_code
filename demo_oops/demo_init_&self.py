 # Here we are going to learn about __init__ and self keyword
class Company:
    def __init__(self,name,salary,age):
        self.name=name
        self.salary=salary
        self.age=age
    def greet(self):
        return f"This Employee name is {self.name} and he is {self.age},he earn {self.salary}"
A=Company("anny",85000,22)
B=Company("pihu",45000,23)
print(A.greet())
print(B.greet())