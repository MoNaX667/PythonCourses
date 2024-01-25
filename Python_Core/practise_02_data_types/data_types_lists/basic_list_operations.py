my_first_list = ["Hello", "Hello" ,33, False, "everybody !"]
print(type(my_first_list))
print(my_first_list)

my_first_list[2]=66
print(my_first_list)

# Append new element
my_first_list.append("New element")
print(my_first_list)

# Sorting
some_numbers = [1, 100, 2, 3, 44, 5, 6]
some_numbers.sort()
print(some_numbers)

# Get length
print(len(some_numbers))

# Extend
some_collection = ["Hello", 2, 3, 4]
some_str = "World"
some_collection.extend(some_str)
print(some_collection)

# Count
print(f"There are {some_collection.count(2)} entries of number '2'")

# Pop & Stack list processing
my_stack = [1, 2, 3]
my_stack.append(4)
my_stack.append(5)
print(f"My original stack {my_stack}")

while(len(my_stack) > 0):
        print(f"Removing stack close elem. Current stack size is {len(my_stack)}")
        my_stack.pop()
        print(f"My stack after removing: {my_stack}")
