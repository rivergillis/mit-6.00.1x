# calculates minimum fixed monthly payment to pay off a debt in 12 months

# test case 1
balance = 3329              # outstanding balance on the credit card
annualInterestRate = 0.2    # annual interest rate

monthlyInterestRate = annualInterestRate / 12.0

guessMinimum = 10
while True:
    testBalance = balance
    for i in range(12):
        testBalance -= guessMinimum
        testBalance += monthlyInterestRate * testBalance
    if testBalance <= 0:
        break
    guessMinimum += 10

print("Lowest Payment: " + str(guessMinimum))
