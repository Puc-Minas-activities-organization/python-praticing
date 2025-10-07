class Prey:
    def flee(self):
        print("This animal is fleeing")

class Predator:
    def hunt(self):
        print("this animal is hunting")

class Rabbits(Prey):
    pass

class Hawks(Predator):
    pass

class Fish(Prey, Predator):
    pass