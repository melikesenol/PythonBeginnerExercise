#   private?

#   in python there's no true private variables

#   _ means you should not touch this this should be private

class PlayerCharacter():
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name} and I am {self.age} years old')


player1 = PlayerCharacter('andrei', 100)

player1.name = '!!!'  # function overrided

player1.speak = 'BOO'  # function overrided
