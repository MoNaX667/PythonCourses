# Input data
proceeds = float(input("Please input your PROCEEDS of your company >>> "))
expenses = float(input("Please input your EXPENSES of your company >>> "))

# Analyzing company's financial results
if proceeds > expenses:
    print("You got a revenue, Please find the detailed information below:")

    # Calculating Profitability per Employee (P/E) and overall profitability
    overall_profitability = proceeds / expenses

    staff_quantity = int(input("Please input number of company's employees >>> "))
    profitability_per_employee = overall_profitability / staff_quantity

    # Outputting profitability details
    print(f"Overall profitability: {overall_profitability}")
    print(f"Calculation information - Employee's quantity {staff_quantity}")
    print(f"Profitability per Employee (P/E): {profitability_per_employee}")

elif proceeds < expenses:
    print("You got a lesion, Need to fix business issues")
else:
    print("It seems you just returned your money back")

