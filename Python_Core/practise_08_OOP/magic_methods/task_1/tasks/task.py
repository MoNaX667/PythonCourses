from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values

    def __add__(self, b):
        counter = 0

        while counter < len(self.values):
            self.values[counter] = f"{self.values[counter]} {b}"
            counter += 1

        return self.values





