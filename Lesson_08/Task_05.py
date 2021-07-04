# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

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


class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, item: "OfficeEquipment"):
        if not isinstance(item, OfficeEquipment):
            raise AddStorageError(f"{item} is not office device")

        self.__storage.append(item)

    def transfer(self, idx: int, department: str):
        item: OfficeEquipment = self.__storage[idx]

        if not isinstance(idx, int):
            raise TransferStorageError(f"It is not allowed type {type(item)}")

        if item.department:
            raise TransferStorageError(f"Equipment {item} has already assigned to the {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for idx, item in enumerate(self):
            a: OfficeEquipment = item
            if all([a.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield idx, item

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


class OfficeEquipment:
    def __init__(
            self,
            eq_type: str,
            vendor: str,
            model: str,
    ):
        self.type = eq_type
        self.vendor = vendor
        self.model = model

        self.department = None

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"


class Printer(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('printer', *args)


class Scanner(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('scanner', *args)


class Xerox(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('xerox', *args)


# Script body
storage = Storage()

storage.add(Printer("HP", "107a"))
storage.add(Scanner("HP", "ScanJet Pro 2500 f1"))
storage.add(Xerox("Xerox", "Work center 5500"))

print(f"Storage balance >>>\n{storage}")

last_index = None

print(">>> Checking the storage for remaining devices")
for index, office_device in storage.filter_by(department=None):
    print(f"{index+1}) {office_device}")
    last_index = index

print(">>> Transfer device to the accountant department")
storage.transfer(last_index, 'Accountant department')
del storage[last_index]

print(">>> Checking the storage for remaining devices")
for index, office_device in storage.filter_by(department=None):
    print(f"{index+1}) {office_device}")

print(f"Storage balance >>>\n{storage}")
