import random  # Import the random module to generate random numbers

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Inform the user that the random number has been generated
print("The random number is generated successfully!")

# Initialize your_number to None to start the guessing game
your_number = None

# Initialize the number of guesses made
guesses = 0

# Start a loop that continues until the correct number is guessed
while(your_number != random_number):
    # Prompt the user to guess a number
    your_number = int(input("Guess the number between 1 to 100: "))
    # Increment the guess count
    guesses += 1

    # Check if the guessed number is correct
    if(your_number == random_number):
        # Inform the user that they guessed correctly and show the number of attempts
        print(f"You have guessed the number {your_number} correctly in {guesses} attempts")

    else:
        # If the guess is too high, prompt the user to guess lower
        if(your_number > random_number):
            print("Lower number please.")
        
        # If the guess is too low, prompt the user to guess higher
        elif(your_number < random_number):
            print("Higher number please.")