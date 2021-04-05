from math import ceil, log

done = False

loan_principal = 0
monthly_payment = 0
loan_interest = 0

while not done:
    print("""
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:"""
)
    choice = input()

    if choice == 'n':
        loan_principal = int(input("Enter the loan principal: "))
        monthly_payment = int(input("Enter the monthly payment: "))
        loan_interest = int(input("Enter the loan interest: "))

        i = loan_interest / (12 * 100)
        months = log(i + 1) * (monthly_payment / (monthly_payment - i * (loan_principal)))
        print(i)
        print(months)
