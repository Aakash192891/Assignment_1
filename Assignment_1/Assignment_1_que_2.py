# python program to compute a person's income tax

gross_income = int(input("Please enter your gross income:"))
number_of_dependents = int(input("Enter the number of dependents:"))
standard_deduction = 10000
dependent_deduction = 3000 
taxable_income = gross_income - standard_deduction - (dependent_deduction*number_of_dependents)

tax_rate = 20/100 

tax = taxable_income*tax_rate 
print(tax) 