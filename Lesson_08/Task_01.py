# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Number(int):
    def __str__(self):
        return f"{self:02}"


class Date:
    date_attributes = ('day', 'month', 'year')

    def __init__(self, date: str, /):
        day, month, year = self.transform(date.split('-'))

        if not self.validate(day, month, year):
            raise ValueError(f"{date} invalid date format")

        self.day = day
        self.month = month
        self.year = year

    def __iter__(self):
        for attribute in self.date_attributes:
            yield self.__getattribute__(attribute)

    @classmethod
    def transform(cls, date):
        return [Number(i) for i in date]

    @staticmethod
    def validate(*date):
        if not all(map(lambda x: isinstance(x, int), date)):
            return False

        day, month, year = date
        return all([1 <= day <= 31, 1 <= month <= 12, year >= 0])

    def __str__(self):
        return f"Date is '{'-'.join([str(s) for s in self])}'"


# Script body
exit_code = None

while exit_code != "Exit":
    user_date = input("Please input any date in format <day>-<month>-<year> or print 'Exit' to close the program >>> ")

    if user_date.lower() == "exit":
        exit_code = "Exit"
        continue
    else:
        try:
            print(Date(user_date))
        except ValueError as e:
            print(f"It seems there is an incorrect date. Please check the exception: {e}")

print("Leaving the program. Have a nice day")
