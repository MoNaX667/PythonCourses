# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.

# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H
# + 0.3). Проверить работу этих методов на реальных данных.

# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    @property
    def full_fabric_square(self):
        return str(f' {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3):.2f}')


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.fabric_square_coat = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Coat square {self.fabric_square_coat}'


class Suit(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.fabric_square_suit = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Suit square {self.fabric_square_suit}'


# Script body
coat = Coat(3, 4)
suit = Suit(4, 7)

# Output
print(f"Coat square {coat}")
print(f"Suit square {suit}")

print(f"Coat full fabric square {coat.full_fabric_square}")
print(f"Suit full fabric square {suit.full_fabric_square}")
