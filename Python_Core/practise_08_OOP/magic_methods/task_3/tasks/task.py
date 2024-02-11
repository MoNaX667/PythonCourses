from __future__ import annotations
from typing import Type


class Currency:
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """

    def __init__(self, value: float):
        self.value = value

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        if cls == other_cls:
            return f"1.0 {cls.__name__} for 1 {cls.__name__}"
        elif cls == Euro:
            if other_cls == Dollar:
                return f"2.0 {other_cls.__name__} for 1 {cls.__name__}"
            elif other_cls == Pound:
                return f"100.0 {other_cls.__name__} for 1 {cls.__name__}"
        elif cls == Dollar:
            if other_cls == Euro:
                return f"0.5 {other_cls.__name__} for 1 {cls.__name__}"
            elif other_cls == Pound:
                return f"50.0 {other_cls.__name__} for 1 {cls.__name__}"
        elif cls == Pound:
            if other_cls == Euro:
                return f"0.01 {other_cls.__name__} for 1 {cls.__name__}"
            elif other_cls == Dollar:
                return f"0.02 {other_cls.__name__} for 1 {cls.__name__}"

    def to_currency(self, other_cls: Type[Currency]) -> Currency:
        if self.__class__ == other_cls:
            return self
        else:
            course_str = self.course(other_cls)
            ratio = float(course_str.split()[0])
            converted_value = self.value * ratio
            return other_cls(converted_value)

    def __add__(self, other: Currency) -> Currency:
        converted_other = other.to_currency(self.__class__)
        return self.__class__(self.value + converted_other.value)

    def __lt__(self, other: Currency) -> bool:
        converted_other = other.to_currency(self.__class__)
        return self.value < converted_other.value

    def __gt__(self, other: Currency) -> bool:
        converted_other = other.to_currency(self.__class__)
        return self.value > converted_other.value

    def __eq__(self, other: Currency) -> bool:
        converted_other = other.to_currency(self.__class__)
        return self.value == converted_other.value

    def __str__(self) -> str:
        currency_symbol = {
            Euro: 'EUR',
            Dollar: 'USD',
            Pound: 'GBP'
        }
        symbol = currency_symbol.get(self.__class__, '')
        return f"{self.value:.1f} {symbol}"


class Euro(Currency):
    pass


class Dollar(Currency):
    pass


class Pound(Currency):
    pass
