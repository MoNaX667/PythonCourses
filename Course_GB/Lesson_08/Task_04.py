# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Storage:
    pass


class OfficeEquipment:
    vat = 0.13
    added_value = 2.0
    retail_rate = 1.3

    def __init__(
            self,
            equipment_type: str,
            vendor: str,
            model: str,
            color: str,
            purchase_price: float,
    ):
        self.type = equipment_type
        self.vendor = vendor
        self.model = model
        self.color = color

        self.purchase_price = purchase_price

        self.printable = True if self.type in ("printer", "xerox") else False
        self.scannable = True if self.type in ("scanner", "xerox") else False

    @property
    def retail_price(self):
        return self.wholesale_price * self.retail_rate

    @property
    def wholesale_price(self):
        return self.purchase_price * (1 + self.vat) * (1 + self.added_value)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model} ({self.color})"


class Printer(OfficeEquipment):
    printable = True
    scannable = False

    def __init__(self, *args):
        super().__init__('printer', *args)


class Scanner(OfficeEquipment):
    printable = False
    scannable = True

    def __init__(self, *args):
        super().__init__('scanner', *args)


class Xerox(OfficeEquipment):
    printable = True
    scannable = True

    def __init__(self, *args):
        super().__init__('xerox', *args)


# Script body
allowed_equipment_types = ("Xerox", "Scanner", "Printer")
equipment_type: str = input("Please choose one of the allowed office equipment(Xerox, Scanner, Printer) >>> ")
equipment_type = equipment_type.lower().capitalize()

if allowed_equipment_types.__contains__(equipment_type):
    vendor_name = input("Please input a new equipment vendor >>> ")
    equipment_model = input("Please input a new equipment model >>> ")
    equipment_color = input("Please input a new equipment color >>> ")

    try:
        equipment_price = float(input("Please input a new equipment price >>> "))
    except ValueError:
        print(f"You tried to input not a number for the price value: {equipment_price}")

    if equipment_type == "Xerox":
        new_user_equipment = Xerox(vendor_name, equipment_model, equipment_color, equipment_price)
    elif equipment_type == "Scanner":
        new_user_equipment = Scanner(vendor_name, equipment_model, equipment_color, equipment_price)
    elif equipment_type == "Printer":
        new_user_equipment = Printer(vendor_name, equipment_model, equipment_color, equipment_price)

    print(f"We added a new office device: {new_user_equipment}")

else:
    print(f"You tried to add a following type of equipment: {equipment_type}. It is not allowed. Please check "
          f"instructions carefully")

print("Leaving the program. Have a nice day")
