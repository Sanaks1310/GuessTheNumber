import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target (1-100) or type 'Quit' to exit: ")
    
    if userChoice.lower() == "quit":
        break

    if not userChoice.isdigit():
        print("Please enter a valid number or 'Quit'.")
        continue

    userChoice = int(userChoice)

    if userChoice == target:
        print("The guess is correct! ")
        break
    elif userChoice < target:
        print("The guess is small. Guess a bigger number.")
    else:
        print("The guess is big. Guess a smaller number.")
   
print("End Of Game")
