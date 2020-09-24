class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, new_surname):
        self._surname = new_surname



class StringD:
    def __init__(self, value=None):
        if value:
            self.set(value)
    
    def set(self, value):
        self._value = value

    
    def get(self):
        return self._value


class Person2:
    def __init__(self, name, surname):
        self.name = StringD(name)
        self.surname = StringD(surname)



# p = Person2('Ivan', 'Ivanov')
# print(p.__dict__)
# print(p.name.get())


from time import time

class Epoch:
    def __get__(self, instance, owner_class):
        return int(time())


class MyTime:
    epoch = Epoch()


# m = MyTime()
# print(m.epoch)

from random import choice

class Dice:
    @property
    def number(self):
        return choice(range(1, 7))


# d = Dice()
# print(d.number)
# print(d.number)
# print(d.number)


class Game:
    @property
    def rock_paper_scissors(self):
        return choice(['rock', 'paper', 'scissors'])

    @property
    def flip(self):
        return choice(['head', 'tails'])

    @property
    def dice(self):
        return choice(range(1, 7))

# d = Game()
# for i in range(3):
#     print(d.dice)
#     print(d.rock_paper_scissors)

# print(d.flip)


class Choice:
    def __init__(self, *choice):
        self._choice = choice

    def __get__(self, obj, owner):
       return choice(self._choice) 


class Game2:
    dice = Choice(1, 2, 3, 4, 5, 6)       
    flip = Choice('heads', 'tails')

d = Game2()
print(d.dice)
print(d.dice)
print(d.dice)
