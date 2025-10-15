class Pet:
    def __init__(self,
                 name,
                 number_of_legs,
                 colour):
        self.name = name
        self.number_of_legs = number_of_legs
        self.colour = colour

    def make_sound(self):
        return ''

    def __str__(self):
        return f'{self.name}'


class Cat(Pet):
    def __init__(self, name, number_of_legs, colour, loves_mices = True):
        super().__init__(name, number_of_legs, colour)
        self.loves_mices = loves_mices

    def make_sound(self):
        return 'Miau, miau'


class Dog(Pet):
    def __init__(self, name, number_of_legs, colour, loves_bones = True):
        super().__init__(name, number_of_legs, colour)
        self.loves_bones = loves_bones

    def make_sound(self):
        return 'Vau, vau'



cat = Cat('Tom', 4, 'Blue-White')
dog = Dog('Goofy', 4, 'Browne', False)

print(cat.make_sound())
print(dog.make_sound())
