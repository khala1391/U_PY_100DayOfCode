class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal __init__ called. Name: {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent class's __init__ method
        super().__init__(name)
        self.breed = breed
        print(f"Dog __init__ called. Breed: {self.breed}")

# Create a Dog instance
dog = Dog("Buddy", "Golden Retriever")
