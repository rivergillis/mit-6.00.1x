# guess the user's number

low = 0
high = 100
guess = (low+high)//2
answer = ""

print("Please think of a number between 0 and 100!")
while (answer != 'c'):
    print("Please think of a number between 0 and 100!")
    print("Is your secret number " + str(guess) + "?")
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if (answer == 'h'):
        high = guess
    elif (answer == 'l'):
        low = guess
    elif (answer == 'c'):
        break
    else:
        print("Sorry, I didn't understand your input.")
    guess = (low+high)//2
print("Game over. Your secret number was: " + str(guess))
