# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()),
# умножение (mul()), деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

class Cell:
    cell_char = 'x'

    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'cell contains {self.quantity * self.cell_char} ({self.quantity}) nucleus'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return Cell(int(self.quantity - other.quantity))
        else:
            return f'Operation is not possible! The result is negative'""

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def order_cell_by(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{f"{self.cell_char}" * cells_in_row}\\n'
        row += f'{f"{self.cell_char}" * (self.quantity % cells_in_row)}'
        return row


# Script body
first_cell = Cell(20)
second_cell = Cell(5)

print(f"First {first_cell}")
print(f"Second {second_cell}")

print(f"The united(sum) {first_cell + second_cell}")
print(f"Subtract second cell from first: {second_cell - first_cell}")
print(f"Subtract first cell from second: {first_cell - second_cell}")

print(f"Try to order cells by 5 {second_cell.order_cell_by(6)}")
print(f"Try to order cells by 6 {first_cell.order_cell_by(6)}")

print(f"First cell div second cell >>> {first_cell / second_cell}")
print(f"First cell div second cell >>> {first_cell / second_cell}")
