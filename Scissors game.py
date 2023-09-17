import random

# Initialize scores
user_score = 0
computer_score = 0


# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "scissors" and computer_choice == "paper")
            or (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

input()



# Main game loop
while True:
    print("\nRock, Paper, Scissors Game")
    print("Choose one: rock, paper, scissors")

    # Get user's choice
    user_choice = input("Your choice: ").lower()

    # Validate user input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    # Generate computer's choice
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine the winner and display the result
    result = determine_winner(user_choice, computer_choice)
    print(result)

    # Update scores
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    # Display current scores
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")

    # Ask if the user wants to play again
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for playing!")

