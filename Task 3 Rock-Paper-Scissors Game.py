import random

def play_rock_paper_scissors():
    
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors game! Let's play!")
    print("Instructions to play this game :")
    print("   - Enter 'rock', 'paper', or 'scissors' to play.")
    print("   - Enter 'quit' to end the game.")
    
    while True:
        # User will give input
        user_choice = input("\nChoose rock, paper, or scissors: ").lower()
        if user_choice == "quit":
            print("\nGame Over!")
            print(f"Final Scores: You: {user_score}, Computer: {computer_score}")
            break
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        # Computer wil choose randomly
        computer_choice = random.choice(["rock", "paper", "scissors"])
        
        # print the choice of both user & computer
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # who is winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        
        # print scores of both 
        print(f"Current Scores: You: {user_score}, Computer: {computer_score}")

        # Ask to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThank you for playing!")
            print(f"Final Scores: You: {user_score}, Computer: {computer_score}")
            break

# Run the game
play_rock_paper_scissors()
