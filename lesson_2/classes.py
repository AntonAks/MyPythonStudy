import random


class Warrior:
    name = 'Warrior'
    health = 100
    strength = 30

    def __init__(self):
        pass

    def punch(self):
        random_attack = random.randint(1, 10)
        attack = random_attack + self.strength
        print(f'PUNCHING ! Attack is - {attack}. ({self.strength} + {random_attack})')
        return attack

    def scream(self):
        self.health = self.health + 5
        print("AAAAAAArrrhhhh !!! (+ 5 to health)")

    def __str__(self):
        return f"name: {self.name}\nhealth: {self.health}\nstrength: {self.strength}"


class Viking(Warrior):
    extra_strength = 10
    extra_health = 30

    def __init__(self, name):
        print(f"\nViking is created! Bonus: strength + {self.extra_strength}, health + {self.extra_health}")
        Warrior.__init__(self)
        self.name = name
        self.strength = self.strength + self.extra_strength
        self.health = self.health + self.extra_health

    def punch(self):
        Warrior.punch(self)
        pass


class Knight(Warrior):
    extra_strength = 5
    extra_health = 40

    def __init__(self, name):
        print(f"\nKnight is created! Bonus: strength + {self.extra_strength}, health + {self.extra_health}")
        Warrior.__init__(self)
        self.name = name
        self.strength = self.strength + self.extra_strength
        self.health = self.health + self.extra_health

    def punch(self):
        Warrior.punch(self)
        pass


# CREATING THE SIMPLE WARRIOR OBJECT
Mark = Warrior()
print(type(Mark))
Mark.scream()
print(str(Mark))
Mark.punch()

# CREATING THE Viking OBJECT which inherited from WARRIOR Class
Erick = Viking('Erick')
print(type(Erick))
Erick.scream()
print(str(Erick))
Erick.punch()

# CREATING THE Knight OBJECT which inherited from WARRIOR Class
Patrick = Knight('Patrick')
print(type(Patrick))
Patrick.scream()
print(str(Patrick))
Patrick.punch()
