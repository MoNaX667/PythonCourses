# Input value and generate necessary nn and nnn numbers
n_number = int(input("Please n number >>>"))
nn_number = int(f"{n_number}{n_number}")
nnn_number = int(f"{n_number}{n_number}{n_number}")

# Calculation
print(f"Calculation: {n_number}+{nn_number}+{nnn_number} = {n_number+nn_number+nnn_number}")