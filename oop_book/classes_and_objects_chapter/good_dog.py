class GoodDog:
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def speak(self):
        return f'{self._name} says Woof!'
    
    def name(self):
        return self._name    # is a getter. I.e. Retrieves name of the instance
    
    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError('Name must be a string')
        self._name = new_name

    def age(self):
        return self._age
    
    def set_age(self, new_age):
        if not isinstance(new_age, int):
            raise TypeError('Age must be an integer')    
        if new_age < 0:
            raise ValueError("Age can't be negative")
        self._age = new_age

    def _dog_years(self):   # Method intended for internal use
        return self.age * 7

sparky = GoodDog('Sparky', 5)
print(sparky.name())    # Sparky
print(sparky.age()) # 5

sparky.set_name('Sage')
print(sparky.name())    # Sage

sparky.set_age(11)
print(sparky.age()) # 11

# sparky.set_name(42) # TypeError: Name must be a string

# sparky.set_age(-1)  # ValueError: Age can't be negative

print(sparky.speak())    # Sage says Woof!

rover = GoodDog('Rover', 3)
print(rover.speak())    # Rover says Woof!