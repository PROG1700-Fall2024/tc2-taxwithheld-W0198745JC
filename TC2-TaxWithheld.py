# Tax Withheld Calculator

# Write a console program that calculates the total amount of tax withheld from an employee’s weekly salary.
# The total withheld tax amount is calculated by combining the amount of provincial tax withheld and the amount of 
# federal tax withheld, minus a per-dependent deduction from the total tax withheld. The user will enter their pre-tax 
# weekly salary amount and the number of dependents they wish to claim. 
# 
# The program will calculate and output the amount of provincial tax withheld, amount of federal tax withheld, the 
# dependent tax deduction, and the user’s final take-home amount.
# Provincial withholding tax is calculated at 6.0%. Federal withholding tax is calculated at 25.0%. 
# The tax deduction for dependents is calculated at 2.0% of the employee’s salary per dependent.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    print("Tax Witholding Calculator")
#define tax amounts
    provincialTax=.06
    federalTax=.25
    dependentTax=.02

#input 
    weeklySalary= float(input("Please enter the amount of your weekly Salary:"))
    dependents= int(input("How Many Dependents do you have?:"))

    provincialWithheld=weeklySalary*provincialTax
    FederalWithheld=weeklySalary*federalTax
    
    if dependents >0:
        dependentDeduction=(dependents*dependentTax)* weeklySalary
    else:
        dependentDeduction= 0

    takeHomePay=(weeklySalary-provincialWithheld)-FederalWithheld+dependentDeduction
    totalWithheld=provincialWithheld+FederalWithheld-dependentDeduction

    print ("Provincial Tax Withheld: ${0:.2f}".format(provincialWithheld))
    print ("Federal Tax Withheld:${0:.2f}".format(FederalWithheld))
    print ("Dependent Deduction for {0} dependents: ${1:.2f}".format(dependents,dependentDeduction))
    print ("Total Withheld: ${0:.2f}".format(totalWithheld))
    print ("Total Take Home: ${0:.2f}".format(takeHomePay))






    # YOUR CODE ENDS HERE

main()
