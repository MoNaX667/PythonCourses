class Person:
    origin_country = "USA"
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce_yourself(self):
        print(f"G: {self.gender}, Age: {self.age}, Name: {self.name}, Country: {self.origin_country}")

    def speak(self, words):
        print(f"[{self.name} speaks] {words}")

list = []
Matt = Person("Matt", 18, "man")
Mike = Person("Mike", 20, "man")
list.append(Matt)
list.append(Mike)

for person in list:
    person.introduce_yourself()

for person in list:
    person.speak("Hello")