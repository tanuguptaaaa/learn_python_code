# Here is an example of inheritance
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Child class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Initialize the parent class
        self.breed = breed

    def speak(self):
        return f"{self.name} barks."

# Creating instances of Animal and Dog
animal = Animal("Generic Animal")
dog = Dog("Buddy", "Golden Retriever")

print(animal.speak())
print(dog.speak())
print(dog.breed)



