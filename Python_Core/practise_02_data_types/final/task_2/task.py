from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    result_table = []
    x_counter = row_start

    while x_counter <= row_end:
        column_table = []
        y_counter = column_start
        print(f"Current y_counter {y_counter} x_counter {x_counter}")

        while y_counter <= column_end:
            print(f"Current c {y_counter} x_counter {x_counter}")
            column_table.append((x_counter * y_counter))
            y_counter += 1

        result_table.append(column_table)
        x_counter += 1

    return result_table
    pass

