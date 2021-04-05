from math import ceil

loan_principal = int(input("Enter the loan principal: "))
done = False

while not done:
    print("What do you want to calculate?")
    print("Type \"m\" - for number of monthly payments,")
    choice = input("Type \"p\" - for the monthly payment "
                   "")

    if choice == 'm':
        monthly_payment = int(input("Enter the monthly payment: "))
        money_left = loan_principal
        months = 0

        while money_left > 0:
            money_left -= monthly_payment
            months += 1
        if money_left <= 0:
            if months == 1:
                print(f'It will take 1 month to pay off the loan')
                done = True
            else:
                print(f'It will take {months} months to pay off the loan')
                done = True
    elif choice == 'p':
        months = int(input("Enter the number of months: "))

        payment = ceil(loan_principal / months)
        if loan_principal % months != 0:
            last_payment = loan_principal - (months - 1) * payment
            print(f'Your monthly payment = {payment} and the last payment = {last_payment}')
            done = True
        else:
            print(f'Your monthly payment = {payment}')
            done = True
        done = True
