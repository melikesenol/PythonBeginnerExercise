#   OOP

class PlayerCharacter:
    #   Class Object Attiribute

    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Tedy', num1 + num2) #   we can instantiate object with cls

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


# player1 = PlayerCharacter("Tom", 20)

# print(player1.adding_things(2,3)) # does not need to initiate player1

player3 = PlayerCharacter.adding_things(2,3)
print(player3.age)
print(player3.name) #   we got name even without initiating

