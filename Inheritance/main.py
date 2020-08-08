#   users can be archers or wizards all the characters in the game


class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking power of {self.power}')


class Archer(User):
    def __init__(self, name, num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_of_arrows}')

    def run(self):
        print('ran really fast')


class HybridBorg(Wizard, Archer):   # multi-inheritance
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

hb1 = HybridBorg('Borgy', 50, 100)
print(hb1.run())
print(hb1.num_of_arrows()) #    errors
print(hb1)
wizard1 = Wizard('Merlin', 50,)
archer1 = Archer('Robin', 100)


print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, Archer))

