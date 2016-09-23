# Problem 1: Paying off debt in a year

# Test case 1:
balance = 42                # outstanding balance on the credit card
annualInterestRate = 0.2    # annual interest rate
monthlyPaymentRate = 0.04   # minimum monthly payment rate -> we pay only min

monthlyInterestRate = annualInterestRate / 12.0

for i in range(12):
    balance -= (monthlyPaymentRate * balance)
    balance += (monthlyInterestRate * balance)

print("Remaining balance: " + str(round(balance, 2)))
