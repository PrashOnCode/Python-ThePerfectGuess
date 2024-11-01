import random

def welcome_message():
    # Display the welcome message to the player
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the randomly generated number within the specified range.")
    print("Good luck!\n")

def choose_difficulty():
    # Allow the player to choose a difficulty level
    print("Choose a difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")
    
    choice = input("Enter the difficulty level (1, 2, or 3): ")
    # Return the maximum number based on the selected difficulty
    if choice == '1':
        return 10
    elif choice == '2':
        return 50
    else:
        return 100

def play_game(max_number):
    # Generate a random number within the specified range
    random_number = random.randint(1, max_number)
    print(f"The random number is generated successfully! (Between 1 and {max_number})")
    
    your_number = None
    guesses = 0
    # Set maximum attempts based on difficulty
    max_attempts = 10 if max_number == 100 else 7  

    while your_number != random_number and guesses < max_attempts:
        # Prompt the player to guess the number
        your_number = int(input(f"Guess the number (attempt {guesses + 1}/{max_attempts}): "))
        guesses += 1

        # Check if the guess is correct
        if your_number == random_number:
            print(f"Congratulations! You have guessed the number {your_number} correctly in {guesses} attempts!")
        elif your_number > random_number:
            print("Lower number please.")
        else:
            print("Higher number please.")
        
        # Provide hints after 3 incorrect guesses
        if guesses > 3:
            if abs(your_number - random_number) <= 10:
                print("You're getting warm!")
            else:
                print("You're cold!")

    # Inform the player if they used all attempts without guessing correctly
    if your_number != random_number:
        print(f"Sorry, you've used all your attempts! The correct number was {random_number}.")

def main():
    # Start the game by displaying the welcome message
    welcome_message()  
    play_again = 'yes'
    
    # Loop to allow the player to play multiple times
    while play_again.lower() in ['yes', 'y']:
        max_number = choose_difficulty()  # Choose difficulty
        play_game(max_number)              # Play the game
        play_again = input("Would you like to play again? (yes/no): ")  # Ask to play again

    print("Thank you for playing! Goodbye!")  # Farewell message

if __name__ == "__main__":
    main()  # Run the main function