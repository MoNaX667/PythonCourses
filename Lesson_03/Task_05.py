# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.

def sum_user_numbers(user_Numbers_String, sumValue = 0):
    """
    Functions sums numbers from user string and return completion execution flag
    :param user_Numbers_String:
    :return: [int, bool]
    """
    user_element_list = user_Numbers_String.split()
    calculation_sum = sumValue
    exit_flag = False

    for element in user_element_list:
        if element == "EXIT":
            exit_flag = True

        try:
            calculation_sum += float(element)
        except ValueError:
            if element != "EXIT":
                print(f"There is not a number - {element}. Be careful")

    return calculation_sum, exit_flag

# Program body
program_sum = 0
program_exit_flag = False

while(program_exit_flag == False):
    user_string = input("Please input a string of numbers separated by whitespaces to get their sum."
                        " Use EXIT command to leave the program >>>")

    function_result = sum_user_numbers(user_Numbers_String=user_string, sumValue=program_sum)

    # Set new program values
    program_sum = function_result[0]
    program_exit_flag = function_result[1]

    # Output results
    print(f"Values were calculated. The sum is {program_sum}")

    if program_exit_flag == True:
        print(f"Have a nice day.")


