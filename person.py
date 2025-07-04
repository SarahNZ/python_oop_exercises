class Person:
    
    def __init__(self, name = 'John Doe'):
        self._name = name

    @property
    def name(self):
        return self._name

person1 = Person()
person2 = Person("Pepe Le Pew")

print(person1.name)
print(person2.name)
