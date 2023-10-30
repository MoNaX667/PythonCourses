# Реализовать два небольших скрипта:
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

# Import functions:
from itertools import cycle

# Data
original_list = ["A", "B", "C"]
result_list = []

# Prepare endless cycle collection
cycle_collection = cycle(original_list)

# Generate limited collection
while len(result_list) < 20:
    result_list.append(next(cycle_collection))

# Output
print(f"Original element collection: {original_list}")
print(f"Result collection of 20 elements: {result_list}")
