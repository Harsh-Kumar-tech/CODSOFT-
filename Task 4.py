import random
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"
def display_results(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    else:
        print("You lose!")
def play_game():
    user_score = 0
    computer_score = 0
    while True:
        print("\n--- Rock, Paper, Scissors Game ---")
        print("Choose one: rock, paper, or scissors (or type 'quit' to exit)")
        user_choice = input("Your choice: ").lower()
        if user_choice == "quit":
            break
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        display_results(user_choice, computer_choice, result)
        print(f"Score - You: {user_score} | Computer: {computer_score}")
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("\nThanks for playing!")
    print(f"Final Score - You: {user_score} | Computer: {computer_score}")
# Start the game
play_game()