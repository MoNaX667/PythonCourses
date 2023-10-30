# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def showUserInfo(Name, Surname, BirthDate, City, Email, PhoneNumber):
    """
    The functions outputs user's info in structured format
    :param Name: User Name
    :param Surname: User Surname
    :param BirthDate: Date of birth
    :param City: User's current city
    :param Email: User's emails address
    :param PhoneNumber: User's phone number
    :return:
    """
    print(f"User info =>>> "
          f"Name: {Name}; "
          f"Surname: {Surname}; "
          f"Date of birth: {BirthDate}; "
          f"City: {City}; "
          f"Email: {Email}; "
          f"PhoneNumber: {PhoneNumber}"
          f"")

showUserInfo(Name="Thomas", City="Prague", Surname="Soweell", BirthDate= "3.4.1965", Email= "strangeUser@corp.com",
             PhoneNumber="232334343")
