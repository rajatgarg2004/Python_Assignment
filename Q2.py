#Take input of the gross income
Gross_income=float(input("Gross Income in Dollars(USD):- "))
#Take input of the number of dependents
Number_of_dependents=int(input("Number of Dependents:- "))
#Taxable income = Gross Income - Standard deduction-(Dependent deduction * No. of dependents)
#Standard Deduction=10000$, Dependent Deduction=3000$
Taxable_income=float(Gross_income-10000-3000*Number_of_dependents)
#Tax = Taxable income * Tax Rate
#Tax Rate=20%
Tax=float(Taxable_income*20/100)
if Tax>0:
    print("Your Tax is ", Tax, "$")
else:
        print('Your income tax is not valid')
