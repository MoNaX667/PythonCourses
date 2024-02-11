class PriceControl:
    """
    Descriptor which doesn't allow to set price
    less than 0 and more than 100 included.
    """

    def __init__(self):
        self._price = None

    def __get__(self, instance, owner):
        return self._price

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Price must be between 0 and 100.")
        else:
            self._price = value


class NameControl:
    """
    Descriptor which doesn't allow to change field value after initialization.
    """

    def __init__(self):
        self._name = None

    def __get__(self, instance, owner):
        return self._name

    def __set__(self, instance, value):
        if self._name is None:
            self._name = value
        else:
            raise ValueError("Name can not be changed.")


class Book:
    author = NameControl()
    name = NameControl()
    price = PriceControl()

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price
