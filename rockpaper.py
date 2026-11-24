
import random

print("=" * 40)
print("     ROCK PAPER SCISSORS")
print("          HUMAN vs AI")
print("=" * 40)

choices = ["rock", "paper", "scissors"]

player_score = 0
ai_score = 0
draws = 0

player_history = []

# Function for AI move
def ai_move():

    # AI observes the player's previous moves
    if len(player_history) >= 2:

        # Find the most recent player move
        last_move = player_history[-1]

        # AI selects the move that beats it
        if last_move == "rock":
            return "paper"

        elif last_move == "paper":
            return "scissors"

        else:
            return "rock"

    # Initially, AI selects randomly
    return random.choice(choices)


# Function to check winner
def check_winner(player, ai):

    if player == ai:
        return "draw"

    elif (
        (player == "rock" and ai == "scissors") or
        (player == "paper" and ai == "rock") or
        (player == "scissors" and ai == "paper")
    ):
        return "player"

    else:
        return "ai"


# Main game
while True:

    print("\nChoose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")

    choice = input("\nEnter your choice (1-4): ").strip()

    if choice == "4":
        break

    if choice not in ["1", "2", "3"]:
        print("Invalid choice! Try again.")
        continue

    player = choices[int(choice) - 1]

    ai = ai_move()

    print("\nYou selected:", player)
    print("AI selected:", ai)

    result = check_winner(player, ai)

    if result == "player":
        print("Congratulations! You won this round!")
        player_score += 1

    elif result == "ai":
        print("AI wins this round! Better luck next time.")
        ai_score += 1

    else:
        print("It's a draw!")
        draws += 1

    # Store player's move for future AI decisions
    player_history.append(player)

    print("\n--- SCOREBOARD ---")
    print("Player:", player_score)
    print("AI:", ai_score)
    print("Draws:", draws)


# Final report
print("\n" + "=" * 40)
print("           FINAL RESULTS")
print("=" * 40)

print("Player Score:", player_score)
print("AI Score:", ai_score)
print("Draws:", draws)

if player_score > ai_score:
    print(" You are the Champion!")

elif ai_score > player_score:
    print(" AI wins the game!")

else:
    print("The game ended in a tie!")

print("\nThank you for playing!")
