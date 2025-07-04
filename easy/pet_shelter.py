class Pet():
    def __init__(self, type, name):
        self._type = type
        self._name = name

    @property
    def type(self):
        return self._type
    
    @property
    def name(self):
        return self._name

class Owner():
    def __init__(self, name):
        self._name = name
        self._pets = []
      
    @property
    def name(self):
        return self._name
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError('The pet must be an instance of the Pet class.')
        self._pets.append(pet)

    def number_of_pets(self):
      return len(self._pets)
    
    def print_pets(self):
        for pet in self._pets:
            print(f"a {pet.type} named {pet.name}")
        
class Shelter():
    def __init__(self):
        self._owners = set() # Track owners who adopted pets (no duplicates)

    def adopt(self, owner, pet):
        owner.add_pet(pet)
        self._owners.add(owner) # to the set

    def print_adoptions(self):
        for owner in self._owners:
            print(f"{owner.name} has adopted the following pets:")
            owner.print_pets()
            print()

cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")

'''
Expected Output

P Hanson has adopted the following pets:
a cat named Cocoa
a cat named Cheddar
a bearded dragon named Darwin

B Holmes has adopted the following pets:
a dog named Molly
a parakeet named Sweetie Pie
a dog named Kennedy
a fish named Chester

P Hanson has 3 adopted pets.
B Holmes has 4 adopted pets.

'''