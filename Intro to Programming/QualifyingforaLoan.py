import math
loan =input("How large is the loan? ")
credit =input("How good is your credit history? ")
income =input("How high is your income? ")
down =input("How large is your down payment? ")
loan_input = int(loan)
credit_input = int(credit)
income_input = int(income)
down_input = int(down)
if loan_input >= 5:
    if credit_input >= 7 and income_input >= 7:
        yes_loan = True
    elif credit_input >= 7 or income_input >= 7:
        if down_input >= 5:
            yes_loan = True
        else:
             yes_loan = False
    else:
         yes_loan =False
else:
    if credit_input < 4:
        yes_loan = False
    else:
        if income_input >= 7 or down_input >= 7:
            yes_loan = True
        elif income_input >= 4 and down_input >= 4:
              yes_loan = True
        else:
              yes_loan = False

if yes_loan:
    print("\n-------------------------------\nLoan Decision: YES")
else:
    print("\n-------------------------------\nLoan Decision: NO")