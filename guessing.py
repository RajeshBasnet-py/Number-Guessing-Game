import random
import time

def display_welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have a limited number of chances to guess the correct number.")
    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    print("4. Exit")

def get_difficulty_level():
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                return 10
            elif choice == 2:
                return 5
            elif choice == 3:
                return 3
            elif choice == 4:
                return 0
            else:
                print("Please choose a valid option (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def start_game(chances):
    secret_number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()

    print(f"\nGreat! You have {chances} chances to guess the correct number.")
    
    while attempts < chances:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess == secret_number:
                end_time = time.time()
                time_taken = round(end_time - start_time, 2)
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                print(f"Time taken: {time_taken} seconds.")
                return attempts

            elif guess < secret_number:
                print(f"Incorrect! The number is greater than {guess}.")
            else:
                print(f"Incorrect! The number is less than {guess}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print(f"\nSorry, you've run out of chances. The correct number was {secret_number}.")
    return attempts

def play_game():
    high_scores = {"easy": float('inf'), "medium": float('inf'), "hard": float('inf')}
    while True:
        display_welcome_message()

        difficulty = get_difficulty_level()

        if difficulty == 0:
            print("Thanks for playing! Goodbye!")
            break
        
        if difficulty == 10:
            level = "easy"
        elif difficulty == 5:
            level = "medium"
        elif difficulty == 3:
            level = "hard"

        print(f"\nLet's start the game with {level.capitalize()} difficulty!")
        
        attempts = start_game(difficulty)

        if attempts < high_scores[level]:
            high_scores[level] = attempts
            print(f"New high score for {level} difficulty! {attempts} attempts.")
        else:
            print(f"High score for {level} difficulty is still {high_scores[level]} attempts.")

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
