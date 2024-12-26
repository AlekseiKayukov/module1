from random import randint


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self.cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        self.cords[0] = dx * self.speed
        self.cords[1] = dy * self.speed

        if dz * self.speed < 0:
            print("It`s too deep, i can`t die :(")
            self.cords[0] = dx
            self.cords[1] = dy
            self.cords[2] = dz
        else:
            self.cords[2] = dz * self.speed

    def get_cords(self):
        print(f"X: {self.cords[0]}, Y: {self.cords[1]}, Z: {self.cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True

    def lay_eggs(self):
        print(f"Here are(is) {randint(1, 4)} eggs for you")

class AquaticAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        new_dz = self.cords[2] - abs(dz) * self.speed / 2
        if new_dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self.cords[2] = new_dz

class PoisonousAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True

db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()