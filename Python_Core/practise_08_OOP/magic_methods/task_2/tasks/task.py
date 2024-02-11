class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return f"{self.name} bird can walk and fly"

    def walk(self):
        return f"{self.name} bird can walk"

    def eat(self):
        return "Birds typically eat various seeds, fruits, and insects."

class FlyingBird(Bird):
    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        return f"It eats mostly {self.ration}"

    def __str__(self):
        return f"{self.name} bird can walk and fly"

class NonFlyingBird(Bird):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        return f"{self.name} cannot fly."

    def swim(self):
        return f"{self.name} bird can swim"

    def eat(self):
        return f"It eats mostly fish"

class SuperBird(NonFlyingBird, FlyingBird):  # Reversed the order of inheritance
    def __init__(self, name, ration="omnivorous"):
        super().__init__(name)
        self.ration = ration

    def swim(self):
        return f"{self.name} bird can swim"

    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"

