class Cat:
    def __init__(self, name):
        self._name = name   # for internal use only

    @property   # getter
    def name(self):
        return self._name
    
    @name.setter    # setter
    def name(self, name):
        if not isinstance(name, str):   # input validation
            raise TypeError('Name must be a string')
        
        self._name = name

    def greet(self):
        print(f"Hello! My name is {self.name}!")

kitty = Cat('Sophie')
kitty.greet()
kitty.name = 'Luna'
kitty.greet()

# Hello! My name is Sophie!
# Hello! My name is Luna!