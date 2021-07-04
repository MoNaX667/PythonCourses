# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


class StorageError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AddStorageError(StorageError):
    def __init__(self, text):
        self.text = f"It is not possible to add to the storage:\n {text}"


class TransferStorageError(StorageError):
    def __init__(self, text):
        self.text = f"Error passing of equipment:\n {text}"


AddStorageError = AddStorageError


class ValidateEquipmentError(StorageError):
    pass


class OfficeEquipment:
    __required_props = ("eq_type", "vendor", "model")

    def __init__(self, eq_type: str = "", vendor: str = "", model: str = ""):
        self.type = eq_type
        self.vendor = vendor
        self.model = model

        self.department = None

    def __setattr__(self, key, value):
        if key in self.__required_props and not value:
            raise AttributeError(f"'{key}' should have not a FALSE value")

        object.__setattr__(self, key, value)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"

    @staticmethod
    def validate(cnt):
        if not isinstance(cnt, int):
            ValidateEquipmentError(f"'{type(cnt)}'; quantity is an int value only!")

    @classmethod
    def create(cls, count, **properties):
        cls.validate(count)
        return [cls(**properties) for _ in range(count)]


class Printer(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Printer', **kwargs)


class Scanner(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Scanner', **kwargs)


class Xerox(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Xerox', **kwargs)


class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, itm: "OfficeEquipment"):
        if not isinstance(itm, OfficeEquipment):
            raise AddStorageError(f"{itm} is not office device")

        self.__storage.append(itm)

    def transfer(self, idx: int, department: str):
        itm: OfficeEquipment = self.__storage[idx]

        if not isinstance(idx, int):
            raise TransferStorageError(f"It is not allowed type {type(itm)}")

        if itm.department:
            raise TransferStorageError(f"Equipment {itm} has already assigned to the {itm.department}")

        itm.department = department

    def filter_by(self, **kwargs):
        for item_index, itm in enumerate(self):
            a: OfficeEquipment = itm
            if all([a.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield item_index, itm

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__storage[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__storage[key]

    def __iter__(self):
        return self.__storage.__iter__()

    def __str__(self):
        return f"Storage has {len(self.__storage)} device(s)"


storage = Storage()

storage.add(Printer(model="550", vendor="HP"))
storage.add(Scanner(model="550-SCAN", vendor="HP"))
storage.add(Xerox(model="34-pro", vendor="XEROX"))

print(storage)
print(f"Getting unassigned office devices >>>")
for index, office_device in storage.filter_by(department=None):
    print(f"{index+1}) {office_device}")

for index, office_device in storage.filter_by(department=None, vendor="HP", model="550"):
    print(f">>> Reserving {office_device} for 'Accountant department'")
    storage.transfer(index, 'Accountant department')

print(storage)

print(f"Getting office devices assigned to the 'Accountant department'>>>")
for index, office_device in storage.filter_by(department='Accountant department'):
    print(f"{index+1}) {office_device}")

print(f"Getting unassigned office devices >>>")
for index, office_device in storage.filter_by(department=None):
    print(f"{index+1}) {office_device}")
