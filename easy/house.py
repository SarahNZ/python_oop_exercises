class House:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def __lt__(self, other):    # less than magic method
        if not isinstance(other, House):
            return NotImplemented
        
        return self.price < other.price
    
    def __gt__(self, other):    # greater than magic method
        if not isinstance(other, House):
            return NotImplemented
        
        return self.price > other.price

sarah_house = House(130565)
eva_house = House(78987451)
if sarah_house < eva_house:
    print("Sarah's home is cheaper")
if eva_house > sarah_house:
    print("Eva's home is more expensive")