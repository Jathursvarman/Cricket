print("By Jathursvarman")
import random

def play_cricket():
    print("Welcome to the Python Cricket Game!")
    print("Rules: You will bat first, and the computer will bowl. Try to score as many runs as possible!")
    print("Enter a number between 1 and 6 for each ball.")

    player_score = 0
    for ball in range(1, 7):  # 6 balls in an over
        try:
            player_input = int(input(f"Ball {ball}: Enter your shot (1-6): "))
            if player_input < 1 or player_input > 6:
                print("Invalid input! Enter a number between 1 and 6.")
                continue
        except ValueError:
            print("Please enter a valid number!")
            continue

        computer_bowl = random.randint(1, 6)
        print(f"Computer bowled: {computer_bowl}")

        if player_input == computer_bowl:
            print("You're out!")
            break
        else:
            player_score += player_input
            print(f"You scored {player_input} runs. Total: {player_score}")

    print("\nComputer's turn to bat! Your target is", player_score + 1)
    computer_score = 0

    for ball in range(1, 7):
        player_bowl = random.randint(1, 6)
        computer_shot = random.randint(1, 6)

        print(f"Ball {ball}: You bowled {player_bowl}, Computer hit {computer_shot}")

        if player_bowl == computer_shot:
            print("You got the computer out!")
            break
        else:
            computer_score += computer_shot
            print(f"Computer scored {computer_shot} runs. Total: {computer_score}")

        if computer_score > player_score:
            print("\nComputer wins!")
            return

    if computer_score == player_score:
        print("\nIt's a tie!")
    else:
        print("\nYou win!")

if __name__ == "__main__":
    play_cricket()
