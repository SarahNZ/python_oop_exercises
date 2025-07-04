class GoodDog():

    def __init__(self, name):
        self.name = name  # self.name is an instance variable (state)
        print(f'Constructor for {self.name}')

    def speak(self):
        print(f'{self.name} says Woof!')

    def roll_over(self):
        print(f'{self.name} is rolling over.')

sparky = GoodDog('Sparky', 5)
rover = GoodDog('Rover', 3)