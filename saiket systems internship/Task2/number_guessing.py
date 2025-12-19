import random

def play_game():
    print("I'm thinking of a number btw 50 and 500")
    print("Try to guess it.\n")

    number = random.randint(50, 500)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < number:
            print("Higher! Try again.\n")
        elif guess > number:
            print("Lower! Try again.\n")
        else:
            print(f"\nCorrect! You guessed it in {attempts} attempts!")
            break


def main():
    while True:
        play_game()

        again = input("\nWanna play again? (y/n): ").strip().lower()

        if again not in ["yes", "y"]:
            print("\nThanks for playing")
            break

    print("Game Ended....")


if __name__ == "__main__":
    main()