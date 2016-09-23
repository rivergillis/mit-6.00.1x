# Finds the minimum monthly payment amount to pay off debt in 12 mo
# Uses bisection search to find the monthly payment to the cent

balance = 30000
annualInterestRate = 0.042

monthlyInterestRate = annualInterestRate / 12.0

guessPaymentLowerBound = balance / 12.0    
guessPaymentUpperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0

epsilon = 0.05
while True:
    testBalance = balance
    guessMonthlyPayment = round(((guessPaymentLowerBound + guessPaymentUpperBound) / 2.0), 2)
    for i in range(12):
        testBalance -= guessMonthlyPayment
        testBalance += (monthlyInterestRate * testBalance)
    testBalance = round(testBalance, 2)
    #print("Final balance for " + str(guessMonthlyPayment) + " is " + str(testBalance))
    if (abs(testBalance) < epsilon) and testBalance <= 0:
        break
    #print("Upper " + str(guessPaymentUpperBound) + "Lower " + str(guessPaymentLowerBound))
    #print("Close? " + str((abs(guessPaymentUpperBound - guessPaymentLowerBound) <= .02)))
    if abs(guessPaymentUpperBound - guessPaymentLowerBound) <= .02:
        break
    if testBalance < epsilon:
        guessPaymentUpperBound = guessMonthlyPayment
        #print("Decreasing upper bound to " + str(guessPaymentUpperBound))
    elif testBalance > epsilon:
        guessPaymentLowerBound = guessMonthlyPayment
        #print("Increasing lower bound to " + str(guessPaymentLowerBound))

print("Lowest Payment: " + str(guessMonthlyPayment))

        
